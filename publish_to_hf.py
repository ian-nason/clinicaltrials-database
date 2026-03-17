#!/usr/bin/env python3
"""Upload clinicaltrials.duckdb to Hugging Face for remote access.

Usage:
    python publish_to_hf.py
    python publish_to_hf.py --db clinicaltrials.duckdb --repo Nason/clinicaltrials-database
    HF_TOKEN=hf_xxx python publish_to_hf.py
"""

import argparse
import sys
from pathlib import Path

import duckdb
from huggingface_hub import HfApi, create_repo


def generate_dataset_card(db_path: str) -> str:
    """Generate a HF-compatible README with YAML frontmatter."""
    con = duckdb.connect(db_path, read_only=True)
    metadata = con.sql(
        "SELECT table_name, description, row_count "
        "FROM _metadata ORDER BY row_count DESC"
    ).fetchdf()
    con.close()

    table_rows = "\n".join(
        f"| `{row['table_name']}` | {row['description']} | {row['row_count']:,} |"
        for _, row in metadata.iterrows()
    )
    total_rows = int(metadata["row_count"].sum())
    n_tables = len(metadata)

    return f"""---
license: cc0-1.0
task_categories:
  - tabular-classification
  - tabular-regression
tags:
  - clinical-trials
  - clinicaltrials-gov
  - aact
  - duckdb
  - medical
  - health
  - government-data
pretty_name: ClinicalTrials.gov Database
size_categories:
  - 10M<n<100M
---

# ClinicalTrials.gov Database (AACT)

A clean, queryable DuckDB database built from the [AACT flat files](https://aact.ctti-clinicaltrials.org/) -- the most comprehensive structured export of ClinicalTrials.gov data.

**{total_rows:,} rows** across **{n_tables} tables** covering every registered clinical trial.

Built with [clinicaltrials-database](https://github.com/ian-nason/clinicaltrials-database).

## Quick Start

### DuckDB CLI

```sql
INSTALL httpfs;
LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/clinicaltrials-database/resolve/main/clinicaltrials.duckdb' AS ct (READ_ONLY);

-- Trials by phase
SELECT overall_status, COUNT(*) as n
FROM ct.studies
GROUP BY overall_status
ORDER BY n DESC;
```

### Python

```python
import duckdb
con = duckdb.connect()
con.sql("INSTALL httpfs; LOAD httpfs;")
con.sql(\"\"\"
    ATTACH 'https://huggingface.co/datasets/Nason/clinicaltrials-database/resolve/main/clinicaltrials.duckdb'
    AS ct (READ_ONLY)
\"\"\")
con.sql("SELECT * FROM ct.studies LIMIT 5").show()
```

DuckDB uses HTTP range requests, so only the pages needed for your query are downloaded.

## Tables

| Table | Description | Rows |
|-------|-------------|------|
{table_rows}

## Data Source

[AACT (Aggregate Analysis of ClinicalTrials.gov)](https://aact.ctti-clinicaltrials.org/) -- maintained by the Clinical Trials Transformation Initiative (CTTI). Updated daily from ClinicalTrials.gov. This is public domain U.S. government data.

## License

Database build code: MIT. Underlying data: public domain (U.S. government work).

## GitHub

Full source code, build instructions, and data dictionary: [github.com/ian-nason/clinicaltrials-database](https://github.com/ian-nason/clinicaltrials-database)
"""


def main():
    parser = argparse.ArgumentParser(
        description="Upload clinicaltrials.duckdb to Hugging Face"
    )
    parser.add_argument(
        "--db", type=Path, default=Path("clinicaltrials.duckdb"),
    )
    parser.add_argument("--repo", default="Nason/clinicaltrials-database")
    parser.add_argument("--token", help="HF token (or set HF_TOKEN env var)")
    args = parser.parse_args()

    if not args.db.exists():
        print(f"Error: Database not found at {args.db}")
        sys.exit(1)

    api = HfApi(token=args.token)

    print(f"Creating dataset repo: {args.repo}")
    create_repo(args.repo, repo_type="dataset", exist_ok=True, token=args.token)

    print(f"Generating dataset card from {args.db}")
    card = generate_dataset_card(str(args.db))

    print("Uploading dataset card...")
    api.upload_file(
        path_or_fileobj=card.encode(),
        path_in_repo="README.md",
        repo_id=args.repo,
        repo_type="dataset",
    )

    size_gb = args.db.stat().st_size / (1024**3)
    print(f"Uploading {args.db} ({size_gb:.1f} GB)...")
    api.upload_file(
        path_or_fileobj=str(args.db),
        path_in_repo="clinicaltrials.duckdb",
        repo_id=args.repo,
        repo_type="dataset",
    )

    print(f"\nUploaded to https://huggingface.co/datasets/{args.repo}")
    print(f"\nUsers can now query remotely:")
    print(
        f"  ATTACH 'https://huggingface.co/datasets/{args.repo}"
        f"/resolve/main/clinicaltrials.duckdb' AS ct (READ_ONLY);"
    )


if __name__ == "__main__":
    main()
