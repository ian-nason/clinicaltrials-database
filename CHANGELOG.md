# Changelog

## 2026-11-16 — Strict source-verified refresh

- Published the November 16 AACT snapshot: 611,764 studies and 59,949,300 stored rows across 48 data tables.
- All 49 archive members strictly parsed; the empty search_results file remains omitted. No malformed records skipped or nonempty coercion losses accepted. Full typed-row hash sums and counts match the source for every table.
- Changed milestones.count_units (BIGINT) and outcome_analyses.ci_lower_limit_raw (DOUBLE) to VARCHAR to retain 29 otherwise unparseable source values. Every prior field remains present; all other source types are unchanged.
- Rechecked every metadata row count, field type and null percentage, study identifiers, all seven date-type labels and working joins. Published the source archive, reproducible bounded builder, dictionary and validation evidence.

## 2026-09-14 — Data refresh (AACT snapshot 2026-09-14)

- Rebuilt from the AACT flat-file export dated 2026-09-14. Total rows
  58,046,170 → 59,028,978 across 48 tables; `studies` 592,206 → 602,514.
- AACT moved its download page (`/pipe_files` → `/downloads`, with a
  site-relative "Download File" link); the builder now finds the export
  there and still accepts the old layout.
- Fix: the header-only `search_results` file recreated an empty phantom table
  (removed by hand in July). The builder now drops every zero-row table, and
  `validate_database.py` fails if `search_results` exists or if any of the
  seven `studies.*_date_type` columns is not VARCHAR with ACTUAL/ESTIMATED.
- DuckDB memory capped at 6 GB with 4 threads (overridable via
  DATAPOND_MEMORY_LIMIT / DATAPOND_THREADS); `publish_to_hf.py --card-only`.

## 2026-07-06 — Full refresh + data-quality audit

Rebuilt from the AACT snapshot of 2026-07-04 and repaired after an
independent SQL-verified audit.

**Data changes**
- 58,046,170 rows across 48 tables; 592,206 studies (through June 2026).

**Fixes**
- All seven `studies.*_date_type` columns restored: they hold
  ACTUAL/ESTIMATED strings and had been silently nulled by date casting.
  Anticipated-vs-actual analyses (reporting timeliness, FDAAA compliance)
  are possible again.
- README example queries corrected: categorical values are AACT's
  UPPER_SNAKE (`'COMPLETED'`, `'PHASE3'`, `'DRUG'`); the phantom
  `has_results` column replaced with
  `calculated_values.were_results_reported`.
- Phantom `search_results` table removed from metadata and the dictionary
  (its source file is header-only and never loads).

**Known caveats** (see README for the full list)
- Results are posted for only ~24% of completed interventional trials.
- No reliable registration time series before 2005 (ICMJE mandate cliff).
- The final snapshot month is right-censored; truncate trends at May 2026.
- Free text uses `~` as a newline surrogate.
