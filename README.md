# ClinicalTrials.gov Database

Explore registered studies from ClinicalTrials.gov through the September 14, 2026 Aggregate Analysis of ClinicalTrials.gov (AACT) snapshot: study designs, conditions, interventions, sponsors, locations, eligibility and reported results. Start with `studies`, which contains 602,514 study records identified by `nct_id`, the ClinicalTrials.gov study identifier (NCT ID); related tables can have many rows per study. Use the database to describe registered research and inspect reported outcomes. Registration and results reporting are incomplete, and this is a frozen registry snapshot rather than individual-patient data or a live feed.

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

The database contains ~50 tables. Key tables include:

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

All tables join on `nct_id` (the ClinicalTrials.gov trial identifier).

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

Results are posted for only ~24% of completed interventional trials — use
`calculated_values.were_results_reported` as the flag (there is no
`has_results` column on `studies`).

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

#### Requirements

- Python 3.9+
- `duckdb` and `requests` packages

#### Build from scratch

```bash
python build_database.py
```

This will download the latest AACT flat file export (~2 GB), extract it, load all tables into DuckDB, create metadata and data dictionary tables, and export DICTIONARY.md.

#### Build from a pre-downloaded zip

```bash
python build_database.py --zip 20260316_export_ctgov.zip
```

#### Build from already-extracted files

```bash
python build_database.py --data-dir ./aact_data
```

#### Validate

```bash
python validate_database.py
```

### Links

- **datapond:** [pypi.org/project/datapond](https://pypi.org/project/datapond/)
- **AACT:** [aact.ctti-clinicaltrials.org](https://aact.ctti-clinicaltrials.org/)
- **ClinicalTrials.gov:** [clinicaltrials.gov](https://clinicaltrials.gov/)
- **Data dictionary:** [DICTIONARY.md](DICTIONARY.md)
