# ClinicalTrials.gov Database

Explore registered studies from ClinicalTrials.gov through the November 16, 2026 Aggregate Analysis of ClinicalTrials.gov (AACT) snapshot: study designs, conditions, interventions, sponsors, locations, eligibility and reported results. Start with `studies`, which contains 611,764 study records identified by `nct_id`, the ClinicalTrials.gov study identifier (NCT ID); related tables can have many rows per study. Use the database to describe registered research and inspect reported outcomes. Registration and results reporting are incomplete, and this is a frozen registry snapshot rather than individual-patient data or a live feed.

<a id="quick-start"></a>

## Start querying

Count study records by their reported status, such as recruiting or completed. These counts describe registered studies, not participants or treatment results.

`overall_status` is the recorded study status; `n` is the number of study records in that status group.

Choose R or Python. Install datapond once: use `install.packages("datapond")` in R, or run `python -m pip install datapond` in a terminal.

### R

```r
library(datapond)
con <- dp_connect("clinicaltrials")
tryCatch({
  DBI::dbExecute(con, "SET threads=1")
  DBI::dbExecute(con, "SET memory_limit='128MiB'")
  DBI::dbExecute(con, "SET max_temp_directory_size='0B'")
  print(DBI::dbGetQuery(con, "SELECT overall_status, COUNT(*) as n
FROM studies
GROUP BY overall_status
ORDER BY n DESC"))
}, finally = dp_disconnect(con))
```

### Python

```python
import datapond
con = datapond.connect('clinicaltrials')
try:
    con.execute("SET threads=1")
    con.execute("SET memory_limit='128MiB'")
    con.execute("SET max_temp_directory_size='0B'")
    print(con.execute("""SELECT overall_status, COUNT(*) as n
FROM studies
GROUP BY overall_status
ORDER BY n DESC""").fetchall())
finally:
    con.close()
```

Queries run on your computer and read the byte ranges they need. A small result can still require a large scan. These examples limit DuckDB to one thread and a 128 MiB buffer pool with disk spill disabled; that is not a limit on the entire R or Python process. Larger analyses may need more memory or a local download with enough disk space.

<a id="additional-dataset-notes"></a>

<a id="tables"></a>

## Tables and joins

The database contains 59,949,300 rows across 48 data tables, including 611,764 studies. Related tables contain repeated records per study, so the total is not a count of studies or participants. Key tables include:

| Table | Description |
|-------|-------------|
| `studies` | Core study record: title, status, phase, type, dates, enrollment |
| `conditions` | Disease or condition names studied in each trial |
| `interventions` | Drugs, devices, procedures, vaccines being tested |
| `sponsors` | Sponsor and collaborator organizations |
| `facilities` | Facility names, locations, and recruiting status |
| `eligibilities` | Participant eligibility criteria (inclusion/exclusion) |
| `designs` | Study design: allocation, masking, assignment |
| `outcomes` | Outcome measure descriptions and time frames |
| `outcome_measurements` | Summary results data by study group |
| `baseline_measurements` | Demographic and baseline measures |
| `reported_events` | Adverse event summaries |
| `countries` | Countries where the study has sites |
| `keywords` | Investigator-provided keywords |
| `browse_conditions` | National Library of Medicine (NLM) Medical Subject Headings (MeSH) terms for conditions |
| `browse_interventions` | NLM-generated MeSH terms for interventions |

Study-related tables join on `nct_id` (the ClinicalTrials.gov study identifier). Lookup tables such as `search_terms` use their own keys; consult the dictionary before joining. Identifiers describe the current snapshot and should not be assumed stable across releases.

See [DICTIONARY.md](DICTIONARY.md) for the full data dictionary with column types, null rates, example values, and join hints.

<a id="coverage-fields-and-sources"></a>

See the [data dictionary](https://github.com/ian-nason/clinicaltrials-database/blob/main/DICTIONARY.md) for column definitions.

## Example queries

> **Value conventions:** categorical columns use AACT's UPPER_SNAKE values —
> `overall_status = 'COMPLETED'` (not `'Completed'`), `phase = 'PHASE3'`,
> `intervention_type = 'DRUG'`. Exceptions exist (`sponsors.lead_or_collaborator`
> is lowercase `'lead'`); check `_columns.example_value` when in doubt.
> Anticipated vs actual dates: every major date has a companion
> `*_date_type` column holding `ACTUAL` or `ESTIMATED`.

### Trials by phase

```sql
SELECT phase, COUNT(*) as trials
FROM studies
WHERE overall_status = 'COMPLETED'
GROUP BY phase
ORDER BY trials DESC;
```

### Top sponsors

```sql
SELECT name, COUNT(*) as trials
FROM sponsors
WHERE lead_or_collaborator = 'lead'
GROUP BY name
ORDER BY trials DESC
LIMIT 20;
```

### Most studied conditions

```sql
SELECT downcase_name, COUNT(*) as trials
FROM conditions
GROUP BY downcase_name
ORDER BY trials DESC
LIMIT 20;
```

### Trials with results by year

In this snapshot, 63,166 of 262,185 completed interventional studies (24.1%) have `calculated_values.were_results_reported = true`. Use that flag; there is no `has_results` column on `studies`. The presence of reported results does not establish their completeness or quality.

```sql
SELECT EXTRACT(YEAR FROM s.completion_date) as year, COUNT(*) as trials
FROM studies s
JOIN calculated_values cv ON s.nct_id = cv.nct_id
WHERE cv.were_results_reported = true
  AND s.completion_date IS NOT NULL
GROUP BY year
ORDER BY year;
```

### Drug intervention records in recruiting Phase 3 studies

This join returns study-intervention-lead-sponsor combinations. A study can appear more than once; the result is not a distinct-study count.

```sql
SELECT s.brief_title, i.name as intervention, sp.name as sponsor
FROM studies s
JOIN interventions i ON s.nct_id = i.nct_id
JOIN sponsors sp ON s.nct_id = sp.nct_id
WHERE s.phase = 'PHASE3'
  AND i.intervention_type = 'DRUG'
  AND sp.lead_or_collaborator = 'lead'
  AND s.overall_status = 'RECRUITING'
LIMIT 20;
```

<a id="advanced-access-quick-start"></a>

## Other ways to connect

### With datapond

```bash
uv pip install datapond
```

```python
import datapond

con = datapond.connect('clinicaltrials')
con.sql("SELECT overall_status, COUNT(*) as n FROM studies GROUP BY 1 ORDER BY 2 DESC").show()
```

### With DuckDB directly

```sql
INSTALL httpfs;
LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/clinicaltrials-database/resolve/main/clinicaltrials.duckdb' AS ct (READ_ONLY);

SELECT * FROM ct.studies LIMIT 5;
```

### Download locally

```python
import datapond
datapond.download('clinicaltrials')

con = datapond.connect('clinicaltrials', local=True)
```

## Snapshot checks and limits

The November 16, 2026 source ZIP contains 49 pipe-delimited files. All were strictly parsed and checked against stored row counts and full typed-row hash sums. The header-only `search_results.txt` is recorded in the audit but does not create a data table. All 48 prior data tables and every prior field remain present. No nonempty value was silently converted to NULL, and no malformed record was skipped.

Two inferred numeric types were corrected to preserve the source text:

- `milestones.count_units`: BIGINT to VARCHAR. Fifteen values contain comma separators or the literal `NA`.
- `outcome_analyses.ci_lower_limit_raw`: DOUBLE to VARCHAR. Fourteen values contain comma separators or unusual spacing. This is a raw source field; these strings are retained without interpreting their intended numeric meaning.

Numeric analyses using these fields now need an explicit, reviewed conversion. All other source column types are unchanged. The seven `studies.*_date_type` columns retain their ACTUAL/ESTIMATED labels. Empty source fields remain NULL; source text, including `~` newline surrogates, is retained. The source is updated daily, while this database is a frozen November 16 snapshot. Registration and result-reporting gaps remain, and the final snapshot month is incomplete.

See [source checks](sources-2026-11-16.json), [release validation](validation-2026-11-16.json), and the [type review](source-type-review-2026-11-16.json) for counts and evidence.

## Sources and maintenance

### Source and license reference

See the [data dictionary](https://github.com/ian-nason/clinicaltrials-database/blob/main/DICTIONARY.md) for column definitions and the [AACT / Clinical Trials Transformation Initiative](https://aact.ctti-clinicaltrials.org/) for the source. License: Public domain.

### Source and license

- **Source:** [AACT / CTTI](https://aact.ctti-clinicaltrials.org/) -- daily export of ClinicalTrials.gov
- **Original data:** [ClinicalTrials.gov](https://clinicaltrials.gov/) (NIH/NLM)
- **Data license:** Public domain (U.S. government data)
- **Build code license:** MIT

### Build source format

The [AACT](https://aact.ctti-clinicaltrials.org/) export supplies pipe-delimited flat files for protocols, conditions, interventions, outcomes, sponsors, facilities, eligibility criteria and results.

### Build instructions

The November 16 release uses Python 3.12 and DuckDB 1.5.5 on Linux/WSL. Download the flat-file ZIP from the [AACT snapshots page](https://aact.ctti-clinicaltrials.org/snapshots) after signing in, or use the original source ZIP archived with the Hugging Face release. AACT also documents API-key downloads for unattended pipelines; keep credentials out of scripts and source control.

```bash
python -m pip install duckdb==1.5.5 requests pytest
python -m pytest test_stream_refresh.py -q
python refresh_20261116.py --archive 20261116_export_ctgov.zip --date 2026-11-16 --output-dir artifacts-2026-11-16
python validate_database.py --db artifacts-2026-11-16/clinicaltrials.duckdb
python validate_release_20261116.py --artifacts artifacts-2026-11-16
```

The builder streams source members through a temporary Unix FIFO. It uses one thread, a 2 GiB DuckDB buffer limit, at most 1 GiB of disk spill, and a 2 GiB free-disk reserve. No full text extraction or copy of the previous database is needed. Buffer limits do not cap total process memory. Start with at least 10 GiB free after obtaining the source ZIP. The schema baseline and reviewed type repairs are included in this repository. `--resume` continues a partial build only when its source hash and baseline match.

The earlier `build_database.py` is retained for historical builds; its unauthenticated download discovery and permissive parser are not the November 16 release path. The original archive hash and package versions are recorded with the release. Raw checks and typed-row fingerprints validate the import; they do not validate the underlying research.

### Links

- **datapond:** [pypi.org/project/datapond](https://pypi.org/project/datapond/)
- **AACT:** [aact.ctti-clinicaltrials.org](https://aact.ctti-clinicaltrials.org/)
- **ClinicalTrials.gov:** [clinicaltrials.gov](https://clinicaltrials.gov/)
- **Data dictionary:** [DICTIONARY.md](DICTIONARY.md)
