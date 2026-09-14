"""Restore the seven studies.*_date_type columns nulled by the date-cast bug
(they hold ACTUAL/ESTIMATED strings; TRY_CAST to DATE silently nulled all of
them — July 2026 audit). Reloads the values from aact_data/studies.txt and
regenerates _columns and DICTIONARY.md."""
from pathlib import Path

import duckdb

from build_database import build_columns_table, export_dictionary

DATE_TYPE_COLS = [
    "study_first_posted_date_type",
    "results_first_posted_date_type",
    "disposition_first_posted_date_type",
    "last_update_posted_date_type",
    "start_date_type",
    "completion_date_type",
    "primary_completion_date_type",
]

con = duckdb.connect("clinicaltrials.duckdb")
con.execute("SET memory_limit = '6GB'")

print("[1/4] Loading date_type values from source")
col_sel = ", ".join(f'"{c}"' for c in DATE_TYPE_COLS)
con.execute(f"""
    CREATE TEMP TABLE _src AS
    SELECT nct_id, {col_sel}
    FROM read_csv('aact_data/studies.txt', delim='|', header=true,
                  all_varchar=true, ignore_errors=true, null_padding=true,
                  max_line_size=10485760, sample_size=10000)
""")
n = con.execute("SELECT COUNT(*) FROM _src").fetchone()[0]
print(f"  {n:,} source rows")

print("[2/4] Retyping columns to VARCHAR and updating")
for c in DATE_TYPE_COLS:
    con.execute(f'ALTER TABLE studies ALTER COLUMN "{c}" SET DATA TYPE VARCHAR')
set_clause = ", ".join(f'"{c}" = NULLIF(TRIM(_src."{c}"), \'\')' for c in DATE_TYPE_COLS)
con.execute(f"""
    UPDATE studies SET {set_clause}
    FROM _src WHERE studies.nct_id = _src.nct_id
""")
con.execute("DROP TABLE _src")

print("[3/4] Verifying")
for c in DATE_TYPE_COLS:
    vals = con.execute(f"""
        SELECT "{c}", COUNT(*) FROM studies GROUP BY 1 ORDER BY 2 DESC
    """).fetchall()
    print(f"  {c}: {vals}")
    non_null = sum(cnt for v, cnt in vals if v is not None)
    assert non_null > 0, f"{c} still empty"
    bad = [v for v, _ in vals if v is not None and v not in ("ACTUAL", "ESTIMATED")]
    assert not bad, f"{c} has unexpected values: {bad}"

print("[4/4] Regenerating _columns and DICTIONARY.md")
# The phantom search_results table (header-only source, never loaded) must
# not appear in metadata or the dictionary.
con.execute("DELETE FROM _metadata WHERE table_name = 'search_results'")
build_columns_table(con)
export_dictionary(con, Path("DICTIONARY.md"))
con.execute("CHECKPOINT")
con.close()
print("DATE_TYPE REPAIR DONE")
