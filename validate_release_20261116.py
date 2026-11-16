"""Check the completed release against its source audit and prior public schema."""
from pathlib import Path
import argparse,json,hashlib
import duckdb
from refresh_20261116 import TYPE_OVERRIDES

ROOT=Path(__file__).resolve().parent

def q(value):return '"'+value.replace('"','""')+'"'

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--artifacts',type=Path,required=True);args=ap.parse_args()
 out=args.artifacts.resolve();source=json.loads((out/'sources-2026-11-16.json').read_text());baseline=json.loads((ROOT/'baseline-2026-11-16.json').read_text())
 assert source['validation']=='passed'
 assert len(source['tables'])==49 and source['table_count']==48
 assert all(not r['coercion_losses'] for r in source['tables'])
 omitted=[r for r in source['tables'] if not r['stored']]
 assert len(omitted)==1 and omitted[0]['table']=='search_results' and omitted[0]['rows']==0
 db=out/'clinicaltrials.duckdb'
 with db.open('rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==source['artifact']['sha256']
 con=duckdb.connect(str(db),read_only=True,config={'threads':'1','memory_limit':'1GiB','max_temp_directory_size':'0B'})
 checks=[]
 try:
  actual={r[0] for r in con.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='main' AND NOT starts_with(table_name,'_')").fetchall()}
  assert actual==set(baseline['schemas'])
  metadata={r[0]:r[1:] for r in con.execute('SELECT table_name,row_count,column_count FROM _metadata').fetchall()}
  for table in sorted(actual):
   schema=con.execute(f'DESCRIBE {q(table)}').fetchall()
   expected_schema=[[r[0],TYPE_OVERRIDES.get((table,r[0]),r[1])] for r in baseline['schemas'][table]]
   assert [list(r[:2]) for r in schema]==expected_schema,table
   rows=con.execute(f'SELECT count(*) FROM {q(table)}').fetchone()[0]
   raw=next(r for r in source['tables'] if r['table']==table)
   assert rows==raw['rows']==metadata[table][0] and len(schema)==metadata[table][1]
   column_meta=con.execute('SELECT column_name,data_type,null_pct,example_value FROM _columns WHERE table_name=?',[table]).fetchall()
   assert {r[0]:r[1] for r in column_meta}=={r[0]:r[1] for r in schema}
   expressions=','.join(f'ROUND(100.0*count(*) FILTER(WHERE {q(r[0])} IS NULL)/count(*),1)' for r in schema)
   nulls=con.execute(f'SELECT {expressions} FROM {q(table)}').fetchone()
   assert dict(zip((r[0] for r in schema),nulls))=={r[0]:r[2] for r in column_meta},table
   checks.append({'table':table,'rows':rows,'previous_rows':baseline['counts'][table],'columns':len(schema),'schema':'reviewed text-field repair' if any(t==table for t,_ in TYPE_OVERRIDES) else 'unchanged','metadata_and_null_rates':'passed'})
  n,distinct=con.execute('SELECT count(*),count(distinct nct_id) FROM studies').fetchone();assert n==distinct==source['studies']
  dates={r[0] for r in baseline['schemas']['studies'] if r[0].endswith('_date_type')};assert len(dates)==7
  date_types={}
  for col in sorted(dates):
   values=con.execute(f'SELECT {q(col)},count(*) FROM studies GROUP BY 1 ORDER BY 1 NULLS LAST').fetchall()
   assert {r[0] for r in values if r[0] is not None}<={'ACTUAL','ESTIMATED'}
   assert any(r[0] is not None for r in values)
   date_types[col]=values
  reporting=con.execute("SELECT count(*),count(*) FILTER(WHERE EXISTS (SELECT 1 FROM calculated_values cv WHERE cv.nct_id=s.nct_id AND cv.were_results_reported=true)) FROM studies s WHERE s.study_type='INTERVENTIONAL' AND s.overall_status='COMPLETED'").fetchone()
  assert reporting[0]>0
  repairs=[]
  review=json.loads((ROOT/'source-type-review-2026-11-16.json').read_text())
  for item in review:
   table,col,typ=item['table'],item['column'],item['previous_type']
   assert TYPE_OVERRIDES[(table,col)]=='VARCHAR'
   values=con.execute(f'SELECT {q(col)},count(*) FROM {q(table)} WHERE {q(col)} IS NOT NULL AND TRY_CAST({q(col)} AS {typ}) IS NULL GROUP BY 1 ORDER BY 1').fetchall()
   assert [list(r) for r in values]==item['values']
   repairs.append({**item,'raw_values_preserved':True})
  joins={}
  for table in ['conditions','sponsors','interventions']:
   joins[table]=con.execute(f'SELECT count(*) FROM {q(table)} c WHERE EXISTS (SELECT 1 FROM studies s WHERE s.nct_id=c.nct_id)').fetchone()[0]
   assert joins[table]>0
  result={'status':'passed','source_snapshot':source['source_snapshot'],'artifact':source['artifact'],'studies':n,'rows':source['rows'],'tables':checks,'date_types':date_types,'completed_interventional_results':{'studies':reporting[0],'with_reported_results':reporting[1],'percent':round(100*reporting[1]/reporting[0],1)},'joined_records':joins,'source_members':49,'empty_source_members':['search_results.txt'],'source_audit':'All source members strictly parsed; counts and full typed-row hash sums matched; no nonempty coercion losses.'}
  result['type_repairs']=repairs
  (out/'validation-2026-11-16.json').write_text(json.dumps(result,indent=2));print('VALIDATED',n,'studies;',source['rows'],'rows in',len(actual),'tables',flush=True)
 finally:con.close()

if __name__=='__main__':main()
