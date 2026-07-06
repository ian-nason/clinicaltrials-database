# Changelog

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
