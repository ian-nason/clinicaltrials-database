#!/usr/bin/env python3
"""Validate the ClinicalTrials.gov DuckDB database.

Runs a series of checks to ensure the database was built correctly.

Usage:
    python validate_database.py
    python validate_database.py --db clinicaltrials.duckdb
"""

import argparse
import sys
from pathlib import Path

import duckdb


EXPECTED_TABLES = [
    "studies",
    "conditions",
    "interventions",
    "outcomes",
    "sponsors",
    "facilities",
    "eligibilities",
    "designs",
    "brief_summaries",
    "detailed_descriptions",
    "countries",
    "keywords",
    "overall_officials",
    "responsible_parties",
    "calculated_values",
    "browse_conditions",
    "browse_interventions",
]


def run_check(name, passed, detail=""):
    """Print a check result."""
    status = "PASS" if passed else "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")
    return passed


def main():
    parser = argparse.ArgumentParser(
        description="Validate the ClinicalTrials.gov DuckDB database"
    )
    parser.add_argument(
        "--db", type=Path, default=Path("clinicaltrials.duckdb"),
        help="Path to the database file",
    )
    args = parser.parse_args()

    if not args.db.exists():
        print(f"Error: Database not found at {args.db}")
        sys.exit(1)

    print(f"Validating {args.db}\n")

    con = duckdb.connect(str(args.db), read_only=True)
    failures = 0

    # 1. Check database opens and has tables
    all_tables = con.execute(
        "SELECT table_name FROM information_schema.tables "
        "WHERE table_schema = 'main' ORDER BY table_name"
    ).fetchall()
    table_names = [t[0] for t in all_tables]
    data_tables = [t for t in table_names if not t.startswith("_")]

    passed = len(data_tables) > 0
    failures += 0 if run_check(
        "Database has data tables", passed, f"{len(data_tables)} tables"
    ) else 1

    # 2. Check expected tables exist
    missing = [t for t in EXPECTED_TABLES if t not in table_names]
    passed = len(missing) == 0
    detail = f"missing: {', '.join(missing)}" if missing else "all present"
    failures += 0 if run_check(
        f"Expected tables ({len(EXPECTED_TABLES)})", passed, detail
    ) else 1

    # 3. Check no empty tables
    empty_tables = []
    for table_name in data_tables:
        count = con.execute(
            f'SELECT COUNT(*) FROM "{table_name}"'
        ).fetchone()[0]
        if count == 0:
            empty_tables.append(table_name)

    passed = len(empty_tables) == 0
    detail = f"empty: {', '.join(empty_tables)}" if empty_tables else "none empty"
    failures += 0 if run_check("No empty tables", passed, detail) else 1

    # 4. Check nct_id in studies
    passed = "studies" in table_names
    if passed:
        cols = con.execute(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_name = 'studies'"
        ).fetchall()
        col_names = [c[0] for c in cols]
        passed = "nct_id" in col_names
    failures += 0 if run_check("nct_id exists in studies", passed) else 1

    # 5. Check studies has data
    if "studies" in table_names:
        count = con.execute("SELECT COUNT(*) FROM studies").fetchone()[0]
        passed = count > 100000
        failures += 0 if run_check(
            "Studies table has substantial data", passed, f"{count:,} rows"
        ) else 1

    # 6. Cross-table join on nct_id
    if "studies" in table_names and "conditions" in table_names:
        join_count = con.execute(
            "SELECT COUNT(*) FROM studies s "
            "JOIN conditions c ON s.nct_id = c.nct_id "
            "LIMIT 1"
        ).fetchone()[0]
        passed = join_count > 0
        failures += 0 if run_check(
            "Cross-table join (studies-conditions)", passed
        ) else 1

    if "studies" in table_names and "sponsors" in table_names:
        join_count = con.execute(
            "SELECT COUNT(*) FROM studies s "
            "JOIN sponsors sp ON s.nct_id = sp.nct_id "
            "LIMIT 1"
        ).fetchone()[0]
        passed = join_count > 0
        failures += 0 if run_check(
            "Cross-table join (studies-sponsors)", passed
        ) else 1

    # 7. Check _metadata table
    passed = "_metadata" in table_names
    if passed:
        meta_count = con.execute("SELECT COUNT(*) FROM _metadata").fetchone()[0]
        passed = meta_count > 0
    failures += 0 if run_check(
        "_metadata table exists and populated", passed,
        f"{meta_count} entries" if passed else "",
    ) else 1

    # 8. Check _columns table
    passed = "_columns" in table_names
    if passed:
        col_count = con.execute("SELECT COUNT(*) FROM _columns").fetchone()[0]
        passed = col_count > 0
    failures += 0 if run_check(
        "_columns table exists and populated", passed,
        f"{col_count} entries" if passed else "",
    ) else 1

    # 9. Check join hints populated
    if "_columns" in table_names:
        hint_count = con.execute(
            "SELECT COUNT(*) FROM _columns WHERE join_hint IS NOT NULL"
        ).fetchone()[0]
        passed = hint_count > 0
        failures += 0 if run_check(
            "Join hints populated in _columns", passed,
            f"{hint_count} columns with hints",
        ) else 1

    # 10. Total row count
    total_rows = con.execute(
        "SELECT SUM(row_count) FROM _metadata"
    ).fetchone()[0]
    print(f"\n  Total rows: {total_rows:,}")
    print(f"  Data tables: {len(data_tables)}")

    db_size = args.db.stat().st_size / (1024**3)
    print(f"  Database size: {db_size:.2f} GB")

    # Summary
    print(f"\n  {'='*40}")
    if failures == 0:
        print("  All checks passed.")
    else:
        print(f"  {failures} check(s) FAILED.")

    con.close()
    sys.exit(1 if failures > 0 else 0)


if __name__ == "__main__":
    main()
