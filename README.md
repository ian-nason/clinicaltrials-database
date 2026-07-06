# ClinicalTrials.gov Database

A clean, queryable DuckDB database built from the [AACT](https://aact.ctti-clinicaltrials.org/) (Aggregate Analysis of ClinicalTrials.gov) pipe-delimited flat files.

Every registered clinical trial in one database: protocols, conditions, interventions, outcomes, sponsors, facilities, eligibility criteria, and results.

## Quick start

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

## Source and license

- **Source:** [AACT / CTTI](https://aact.ctti-clinicaltrials.org/) -- daily export of ClinicalTrials.gov
- **Original data:** [ClinicalTrials.gov](https://clinicaltrials.gov/) (NIH/NLM)
- **Data license:** Public domain (U.S. government data)
- **Build code license:** MIT

## Tables

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
| `browse_conditions` | NLM-generated MeSH terms for conditions |
| `browse_interventions` | NLM-generated MeSH terms for interventions |

All tables join on `nct_id` (the ClinicalTrials.gov trial identifier).

See [DICTIONARY.md](DICTIONARY.md) for the full data dictionary with column types, null rates, example values, and join hints.

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

### Drug trials in Phase 3

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

## Build instructions

### Requirements

- Python 3.9+
- `duckdb` and `requests` packages

### Build from scratch

```bash
python build_database.py
```

This will download the latest AACT flat file export (~2 GB), extract it, load all tables into DuckDB, create metadata and data dictionary tables, and export DICTIONARY.md.

### Build from a pre-downloaded zip

```bash
python build_database.py --zip 20260316_export_ctgov.zip
```

### Build from already-extracted files

```bash
python build_database.py --data-dir ./aact_data
```

### Validate

```bash
python validate_database.py
```

## Links

- **datapond:** [pypi.org/project/datapond](https://pypi.org/project/datapond/)
- **AACT:** [aact.ctti-clinicaltrials.org](https://aact.ctti-clinicaltrials.org/)
- **ClinicalTrials.gov:** [clinicaltrials.gov](https://clinicaltrials.gov/)
- **Data dictionary:** [DICTIONARY.md](DICTIONARY.md)
