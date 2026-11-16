"""Strict, disk-bounded AACT refresh from an explicitly downloaded source ZIP.

The source archive is streamed through a temporary Unix FIFO, one member at a
time. No full CSV extraction or copy of the prior database is required.
"""
from pathlib import Path
import argparse,csv,hashlib,io,json,os,shutil,tempfile,threading,zipfile
import duckdb
import build_database as legacy

ROOT=Path(__file__).resolve().parent
# These source fields contain text that the previous inferred numeric types
# cannot represent. Preserve every raw value, including separators and "NA".
TYPE_OVERRIDES={('milestones','count_units'):'VARCHAR',('outcome_analyses','ci_lower_limit_raw'):'VARCHAR'}
def q(value):return '"'+value.replace('"','""')+'"'
def lit(value):return "'"+str(value).replace("'","''")+"'"
def sha(path):
 with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()

def stream_sql(con,archive,member,columns,sql):
 """Read a ZIP member once, propagating CRC, writer and strict CSV errors."""
 errors=[]
 with tempfile.TemporaryDirectory(prefix='datapond-aact-') as tmp:
  fifo=Path(tmp)/'source.pipe';os.mkfifo(fifo)
  def write():
   try:
    with zipfile.ZipFile(archive) as z,z.open(member) as src,fifo.open('wb') as dst:
     shutil.copyfileobj(src,dst,length=1024*1024)
   except BaseException as e:errors.append(e)
  worker=threading.Thread(target=write,daemon=True);worker.start()
  mapping='{'+','.join(lit(col)+":'VARCHAR'" for col in columns)+'}'
  source=f"read_csv({lit(fifo)},delim='|',header=true,columns={mapping},auto_detect=false,quote='\"',escape='\"',nullstr='',strict_mode=true,ignore_errors=false,null_padding=false,max_line_size=10485760)"
  try:result=con.execute(sql.format(source=source)).fetchall()
  finally:worker.join(timeout=10)
  assert not worker.is_alive(),'Source writer did not complete'
  if errors:raise errors[0]
  return result

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--archive',type=Path,required=True);ap.add_argument('--date',required=True);ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--resume',action='store_true');args=ap.parse_args()
 assert duckdb.__version__=='1.5.5'
 assert len(args.date)==10 and args.date[:4]=='2026'
 archive=args.archive.resolve();out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=True);db=out/'clinicaltrials.duckdb';assert db.exists()==args.resume
 baseline=json.loads((ROOT/'baseline-2026-11-16.json').read_text());schemas=baseline['schemas']
 assert shutil.disk_usage(out).free > (0 if args.resume else baseline['bytes'])+2*1024**3,'Insufficient free space for the database and a 2 GiB reserve'
 with zipfile.ZipFile(archive) as z:
  members={Path(n).stem.lower():n for n in z.namelist() if n.lower().endswith('.txt') and not n.endswith('/')}
  assert len(members)==len([n for n in z.namelist() if n.lower().endswith('.txt') and not n.endswith('/')]),'Duplicate source table names'
  assert set(schemas)<=set(members),'Source omits prior tables: '+str(set(schemas)-set(members))
  headers={}
  for table,member in members.items():
   with z.open(member) as f:
    header=next(csv.reader(io.TextIOWrapper(f,encoding='utf-8-sig'),delimiter='|'))
   assert len(header)==len(set(header)) and all(header)
   headers[table]=header
 c=duckdb.connect(str(db),config={'threads':'1','memory_limit':'2GiB','max_temp_directory_size':'1GiB','preserve_insertion_order':'false'});c.execute("SET checkpoint_threshold='1GiB'")
 report={'source_snapshot':args.date,'source_page':'https://aact.ctti-clinicaltrials.org/snapshots','archive':{'filename':archive.name,'bytes':archive.stat().st_size,'sha256':sha(archive)},'baseline':{'revision':baseline['revision'],'sha256':baseline['sha256']},'source_member_count':len(members),'tables':[],'validation':'in_progress'}
 if args.resume:
  saved=json.loads((out/'sources-2026-11-16.json').read_text())
  assert saved['archive']==report['archive'] and saved['baseline']==report['baseline'] and saved['source_snapshot']==args.date
  assert saved['validation']=='in_progress'
  report['tables']=saved['tables']
 report['type_changes']=[{'table':t,'column':col,'from':next(r[1] for r in schemas[t] if r[0]==col),'to':typ,'reason':'Preserve nonempty source text that does not parse under the prior inferred numeric type.'} for (t,col),typ in TYPE_OVERRIDES.items()]
 built=[]
 try:
  for table in sorted(members):
   assert table.replace('_','').isalnum(),table
   header=headers[table];prior={row[0]:row[1] for row in schemas.get(table,[])}
   assert set(prior)<=set(header),'Prior source fields missing: '+table+': '+str(set(prior)-set(header))
   types={col:TYPE_OVERRIDES.get((table,col),prior.get(col,'VARCHAR')) for col in header}
   saved=next((r for r in report['tables'] if r['table']==table),None)
   if saved and not saved['coercion_losses']:
    if saved['stored']:
     assert c.execute(f'SELECT count(*) FROM {q(table)}').fetchone()[0]==saved['rows']
     assert {r[0]:r[1] for r in c.execute(f'DESCRIBE {q(table)}').fetchall()}==types
     built.append(table)
    print('RESUMED verified table',table,flush=True);continue
   if saved:
    c.execute(f'DROP TABLE IF EXISTS {q(table)}')
    report['tables']=[r for r in report['tables'] if r['table']!=table]
   projection=','.join(f'TRY_CAST({q(col)} AS {typ}) AS {q(col)}' for col,typ in types.items())
   stream_sql(c,archive,members[table],header,f'CREATE TABLE {q(table)} AS SELECT {projection} FROM {{source}}')
   columns=','.join(q(col) for col in header)
   expected=c.execute(f'SELECT count(*),sum(hash({columns})::HUGEINT) FROM {q(table)}').fetchone()
   losses=[(col,typ) for col,typ in types.items() if typ!='VARCHAR']
   loss_terms=','.join(f'count(*) FILTER(WHERE {q(col)} IS NOT NULL AND TRY_CAST({q(col)} AS {typ}) IS NULL)' for col,typ in losses)
   # Compare raw parse count and a full typed-row fingerprint on a second stream.
   observed=stream_sql(c,archive,members[table],header,f'SELECT count(*),sum(hash({columns})::HUGEINT) FROM (SELECT {projection} FROM {{source}})')[0]
   assert observed==expected,'Source comparison failed: '+table
   # A separate bounded pass makes all coercion loss explicit; none is accepted silently.
   counts=stream_sql(c,archive,members[table],header,'SELECT '+loss_terms+' FROM {source}')[0] if losses else []
   lost={col:n for (col,_),n in zip(losses,counts) if n}
   rec={'table':table,'member':members[table],'rows':expected[0],'columns':len(header),'new_fields':sorted(set(header)-set(prior)),'coercion_losses':lost,'source_comparison':'Strict parse count and full typed-row hash sum match','typed_row_hash_sum':str(expected[1]),'stored':expected[0]>0 or table in schemas}
   report['tables'].append(rec);(out/'sources-2026-11-16.json').write_text(json.dumps(report,indent=2,default=str));print(table,expected[0],'losses',lost,flush=True)
   assert not lost,'Nonempty values lost in existing types; review required: '+table
   if rec['stored']:built.append(table)
   else:c.execute(f'DROP TABLE {q(table)}')
   c.execute('CHECKPOINT')
   assert shutil.disk_usage(out).free>2*1024**3,'Free space dropped below 2 GiB reserve'
  legacy.build_metadata(c,built,members);legacy.build_columns_table(c);legacy.export_dictionary(c,out/'DICTIONARY.md')
  study_rows,study_ids=c.execute('SELECT count(*),count(distinct nct_id) FROM studies').fetchone();assert study_rows==study_ids and study_rows>100000
  report.update(rows=sum(r['rows'] for r in report['tables']),table_count=len(built),studies=study_rows,validation='passed');c.execute('CHECKPOINT')
 finally:c.close()
 report['artifact']={'bytes':db.stat().st_size,'sha256':sha(db)};(out/'sources-2026-11-16.json').write_text(json.dumps(report,indent=2,default=str));print('COMPLETE',report['rows'],flush=True)

if __name__=='__main__':main()
