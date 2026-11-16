import tempfile,zipfile,duckdb
from pathlib import Path
from refresh_20261116 import stream_sql

def test_quoted_multiline_and_unicode():
 with tempfile.TemporaryDirectory() as folder:
  zpath=Path(folder)/'source.zip'
  with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
   z.writestr('sample.txt','id|text\n1|"a|b"\n2|"first\nsecond"\n3|é\n4|\n')
  con=duckdb.connect()
  try:
   rows=stream_sql(con,zpath,'sample.txt',['id','text'],'SELECT CAST(id AS BIGINT), text FROM {source}')
   assert rows==[(1,'a|b'),(2,'first\nsecond'),(3,'é'),(4,None)]
  finally:con.close()

def test_source_coercion_is_visible():
 with tempfile.TemporaryDirectory() as folder:
  zpath=Path(folder)/'source.zip'
  with zipfile.ZipFile(zpath,'w') as z:z.writestr('sample.txt','id\n1\nnot-a-number\n')
  con=duckdb.connect()
  try:
   rows=stream_sql(con,zpath,'sample.txt',['id'],'SELECT count(*) FILTER(WHERE id IS NOT NULL AND TRY_CAST(id AS BIGINT) IS NULL) FROM {source}')
   assert rows==[(1,)]
  finally:con.close()
