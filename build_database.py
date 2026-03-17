#!/usr/bin/env python3
"""Build a DuckDB database from the AACT ClinicalTrials.gov pipe-delimited flat files.

Downloads the latest export from AACT (Aggregate Analysis of ClinicalTrials.gov),
loads all pipe-delimited .txt files into DuckDB, creates metadata and data dictionary
tables, and exports DICTIONARY.md.

Usage:
    python build_database.py
    python build_database.py --data-dir ./aact_data
    python build_database.py --zip 20260316_export_ctgov.zip
    python build_database.py --output clinicaltrials.duckdb
"""

import argparse
import io
import os
import re
import sys
import time
import zipfile
from pathlib import Path

import duckdb
import requests

DOWNLOAD_PAGE = "https://aact.ctti-clinicaltrials.org/downloads"
SOURCE_URL = "https://aact.ctti-clinicaltrials.org/"
LICENSE = "Public domain"

# Tables that should always exist if the data is complete
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

# Table descriptions (from AACT data dictionary)
TABLE_DESCRIPTIONS = {
    "studies": "Core study record: title, status, phase, type, dates, enrollment, and regulatory info",
    "brief_summaries": "Brief text summary of the study protocol",
    "detailed_descriptions": "Detailed text description of the study protocol",
    "eligibilities": "Participant eligibility criteria (inclusion/exclusion, age, sex)",
    "designs": "Study design details: allocation, masking, assignment, purpose",
    "conditions": "Disease or condition names studied in each trial",
    "interventions": "Interventions or exposures: drugs, devices, procedures, vaccines",
    "intervention_other_names": "Synonymous names for interventions",
    "design_groups": "Protocol-specified groups or cohorts assigned to interventions",
    "design_group_interventions": "Cross-reference mapping design groups to interventions",
    "design_outcomes": "Planned outcome measures and observations",
    "browse_conditions": "NLM-generated MeSH terms for study conditions",
    "browse_interventions": "NLM-generated MeSH terms for study interventions",
    "keywords": "Investigator-provided keywords describing the study",
    "facilities": "Facility names, addresses, and recruiting status",
    "facility_contacts": "Contact information at each study facility",
    "facility_investigators": "Investigator names at each study facility",
    "countries": "Countries where the study has sites",
    "sponsors": "Sponsor and collaborator names and types",
    "central_contacts": "Primary and backup contacts for enrollment questions",
    "overall_officials": "People responsible for overall scientific leadership",
    "responsible_parties": "Parties responsible for submitting study information",
    "id_information": "Identifiers other than NCT ID (org study IDs, secondary IDs)",
    "calculated_values": "AACT-computed fields: months to report results, facilities count, etc.",
    "links": "Web links relevant to the study",
    "study_references": "Citations to publications related to the study",
    "outcomes": "Outcome measure descriptions and time frames",
    "outcome_measurements": "Summary data for outcome measures by study group",
    "outcome_counts": "Sample sizes for each outcome by study group",
    "outcome_analyses": "Statistical analyses performed on outcomes",
    "outcome_analysis_groups": "Groups involved in each outcome analysis",
    "baseline_counts": "Sample sizes at baseline for each study group",
    "baseline_measurements": "Demographic and baseline measures by group",
    "result_groups": "Aggregate list of group titles/descriptions for results reporting",
    "milestones": "Participant progress through each stage of the study",
    "drop_withdrawals": "Summary of participant withdrawals: counts and reasons",
    "participant_flows": "Recruitment and pre-assignment details",
    "reported_events": "Summary of reported adverse events",
    "reported_event_totals": "Totals of reported adverse events by category",
    "result_agreements": "Agreements between sponsor and principal investigators about results",
    "result_contacts": "Points of contact for scientific information about results",
    "pending_results": "Events related to submission of results for QC review",
    "documents": "Full study protocol and statistical analysis plan",
    "provided_documents": "Protocol, SAP, and informed consent form documents",
    "ipd_information_types": "Individual participant data sharing information types",
    "search_results": "Joins studies with saved queries",
    "study_searches": "Saved queries used to search ClinicalTrials.gov",
    "retractions": "Retraction notices for study results or publications",
    "result_derivations": "How results were derived from reported data",
}

# Known join hints
JOIN_HINTS = {
    "nct_id": "Primary trial identifier, joins across all AACT tables",
    "id": "Table primary key (auto-increment)",
    "outcome_id": "Joins to outcomes.id",
    "result_group_id": "Joins to result_groups.id",
    "milestone_id": "Joins to milestones.id",
    "facility_id": "Joins to facilities.id",
    "intervention_id": "Joins to interventions.id",
    "design_group_id": "Joins to design_groups.id",
    "outcome_analysis_id": "Joins to outcome_analyses.id",
    "document_id": "Joins to documents.id",
}

# Columns that look like dates based on name patterns
DATE_PATTERNS = [
    r"_date$",
    r"_date_type$",
    r"date_",
    r"^start_date$",
    r"^completion_date$",
    r"^verification_date$",
    r"^posted_date$",
    r"^created_at$",
    r"^updated_at$",
    r"^first_received_date$",
    r"^last_changed_date$",
]


def find_download_url():
    """Scrape the AACT downloads page to find the flat file zip URL."""
    print("  Checking AACT downloads page...")
    try:
        resp = requests.get(DOWNLOAD_PAGE, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"  Error fetching download page: {e}")
        return None

    # Look for download links with the flat file pattern
    # The flat file download has: download="YYYYMMDD_export_ctgov.zip" href="URL"
    # The postgres dump has: download="YYYYMMDD_clinical_trials_ctgov.zip" href="URL"
    text = resp.text

    # Best match: look for download attribute containing "export_ctgov"
    match = re.search(
        r'download="[^"]*export_ctgov[^"]*"[^>]*href="'
        r'(https://ctti-aact\.nyc3\.digitaloceanspaces\.com/[a-z0-9]+)',
        text,
    )
    if match:
        return match.group(1)

    # Alternate: look for "snapshot-card flatfiles" section
    match = re.search(
        r'snapshot-card flatfiles.*?href="'
        r'(https://ctti-aact\.nyc3\.digitaloceanspaces\.com/[a-z0-9]+)',
        text,
        re.DOTALL,
    )
    if match:
        return match.group(1)

    # Last resort: all URLs, skip postgres and covid
    urls = re.findall(
        r'https://ctti-aact\.nyc3\.digitaloceanspaces\.com/[a-z0-9]+',
        text,
    )
    for url in urls:
        idx = text.find(url)
        before = text[max(0, idx - 300):idx].lower()
        if "clinical_trials_ctgov" not in before and "covid" not in before:
            return url

    return urls[0] if urls else None


def download_zip(url, dest_path):
    """Download the zip file with progress reporting."""
    print(f"  Downloading from {url}")
    resp = requests.get(url, stream=True, timeout=30)
    resp.raise_for_status()

    total = int(resp.headers.get("content-length", 0))
    downloaded = 0

    with open(dest_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=1024 * 1024):
            f.write(chunk)
            downloaded += len(chunk)
            if total > 0:
                pct = int(downloaded * 100 / total)
                mb = downloaded / (1024 * 1024)
                total_mb = total / (1024 * 1024)
                print(
                    f"\r  {mb:.0f} / {total_mb:.0f} MB ({pct}%)",
                    end="",
                    flush=True,
                )
    print()
    return dest_path


def extract_zip(zip_path, dest_dir):
    """Extract all .txt files from the zip."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    txt_files = []

    with zipfile.ZipFile(zip_path, "r") as zf:
        members = [m for m in zf.namelist() if m.endswith(".txt")]
        print(f"  Found {len(members)} .txt files in zip")

        for member in members:
            zf.extract(member, dest_dir)
            extracted = dest_dir / member
            txt_files.append(extracted)

    return txt_files


def discover_txt_files(data_dir):
    """Find all .txt files in the data directory."""
    txt_files = sorted(data_dir.rglob("*.txt"))
    return txt_files


def table_name_from_file(filepath):
    """Derive table name from filename."""
    return filepath.stem.lower()


def load_table(con, table_name, filepath):
    """Load a pipe-delimited .txt file into a DuckDB table.

    Returns the number of rows loaded, or 0 on failure.
    """
    try:
        # First, check if the file is empty or has no data rows
        file_size = filepath.stat().st_size
        if file_size == 0:
            return 0

        # Use DuckDB's CSV reader with pipe delimiter
        con.execute(f"""
            CREATE OR REPLACE TABLE "{table_name}" AS
            SELECT * FROM read_csv(
                '{filepath}',
                delim='|',
                header=true,
                auto_detect=true,
                ignore_errors=true,
                null_padding=true,
                max_line_size=10485760,
                sample_size=10000
            )
        """)

        row_count = con.execute(
            f'SELECT COUNT(*) FROM "{table_name}"'
        ).fetchone()[0]
        return row_count

    except Exception as e:
        print(f"    WARNING: Failed to load {table_name}: {e}")
        return 0


def cast_date_columns(con, table_name):
    """Try to cast columns that look like dates."""
    cols = con.execute(
        f"SELECT column_name, data_type FROM information_schema.columns "
        f"WHERE table_name = '{table_name}' AND table_schema = 'main'"
    ).fetchall()

    for col_name, dtype in cols:
        if dtype != "VARCHAR":
            continue

        is_date_col = any(
            re.search(pattern, col_name.lower()) for pattern in DATE_PATTERNS
        )
        if not is_date_col:
            continue

        # Try casting to DATE
        try:
            # Check if values look like dates
            sample = con.execute(
                f'SELECT "{col_name}" FROM "{table_name}" '
                f'WHERE "{col_name}" IS NOT NULL LIMIT 100'
            ).fetchall()

            if not sample:
                continue

            # Try the cast on the sample first
            con.execute(
                f'SELECT TRY_CAST("{col_name}" AS DATE) '
                f'FROM "{table_name}" '
                f'WHERE "{col_name}" IS NOT NULL LIMIT 10'
            )

            # If that worked, alter the column
            con.execute(f"""
                ALTER TABLE "{table_name}"
                ALTER COLUMN "{col_name}"
                SET DATA TYPE DATE
                USING TRY_CAST("{col_name}" AS DATE)
            """)
        except Exception:
            pass


def build_metadata(con, built_tables, file_map):
    """Create the _metadata table."""
    con.execute("DROP TABLE IF EXISTS _metadata")
    con.execute("""
        CREATE TABLE _metadata (
            table_name VARCHAR,
            source_file VARCHAR,
            source_url VARCHAR,
            description VARCHAR,
            row_count BIGINT,
            column_count INTEGER,
            license VARCHAR,
            built_at TIMESTAMP
        )
    """)

    for table_name in sorted(built_tables):
        row_count = con.execute(
            f'SELECT COUNT(*) FROM "{table_name}"'
        ).fetchone()[0]
        col_count = con.execute(
            f"SELECT COUNT(*) FROM information_schema.columns "
            f"WHERE table_name = '{table_name}' AND table_schema = 'main'"
        ).fetchone()[0]

        source_file = file_map.get(table_name, "")
        description = TABLE_DESCRIPTIONS.get(table_name, "")

        con.execute(
            "INSERT INTO _metadata VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)",
            [
                table_name,
                source_file,
                SOURCE_URL,
                description,
                row_count,
                col_count,
                LICENSE,
            ],
        )


def build_columns_table(con):
    """Build the _columns data dictionary table."""
    con.execute("DROP TABLE IF EXISTS _columns")

    con.execute("""
        CREATE TABLE _columns AS
        SELECT
            c.table_name,
            c.column_name,
            c.data_type,
            m.source_file
        FROM information_schema.columns c
        LEFT JOIN _metadata m ON m.table_name = c.table_name
        WHERE c.table_schema = 'main'
          AND c.table_name NOT IN ('_metadata', '_columns')
    """)

    con.execute("ALTER TABLE _columns ADD COLUMN example_value VARCHAR")
    con.execute("ALTER TABLE _columns ADD COLUMN join_hint VARCHAR")
    con.execute("ALTER TABLE _columns ADD COLUMN null_pct DOUBLE")

    # Apply join hints
    for col, hint in JOIN_HINTS.items():
        con.execute(
            "UPDATE _columns SET join_hint = ? WHERE column_name = ?",
            [hint, col],
        )

    # Populate example_value and null_pct
    rows = con.execute(
        "SELECT table_name, column_name FROM _columns"
    ).fetchall()
    total = len(rows)

    for i, (table_name, column_name) in enumerate(rows):
        if (i + 1) % 100 == 0:
            print(f"  Enriching columns: {i + 1}/{total}", flush=True)

        # Example value
        try:
            result = con.execute(
                f'SELECT CAST("{column_name}" AS VARCHAR) '
                f'FROM "{table_name}" '
                f'WHERE "{column_name}" IS NOT NULL LIMIT 1'
            ).fetchone()
            if result:
                val = result[0]
                if len(val) > 80:
                    val = val[:77] + "..."
                con.execute(
                    "UPDATE _columns SET example_value = ? "
                    "WHERE table_name = ? AND column_name = ?",
                    [val, table_name, column_name],
                )
        except Exception:
            pass

        # Null percentage
        try:
            result = con.execute(
                f'SELECT ROUND(100.0 * COUNT(*) FILTER '
                f'(WHERE "{column_name}" IS NULL) / COUNT(*), 1) '
                f'FROM "{table_name}"'
            ).fetchone()
            if result and result[0] is not None:
                con.execute(
                    "UPDATE _columns SET null_pct = ? "
                    "WHERE table_name = ? AND column_name = ?",
                    [result[0], table_name, column_name],
                )
        except Exception:
            pass


def export_dictionary(con, output_path):
    """Export _columns and _metadata as a readable DICTIONARY.md file."""
    lines = []
    lines.append("# Data Dictionary")
    lines.append("")
    lines.append(
        "Source: [AACT (Aggregate Analysis of ClinicalTrials.gov)]"
        "(https://aact.ctti-clinicaltrials.org/)"
    )
    lines.append("")

    tables = con.execute(
        "SELECT DISTINCT table_name FROM _columns ORDER BY table_name"
    ).fetchall()

    for (table_name,) in tables:
        meta = con.execute(
            "SELECT row_count, source_file, description "
            "FROM _metadata WHERE table_name = ?",
            [table_name],
        ).fetchone()

        lines.append(f"## {table_name}")
        lines.append("")
        if meta:
            row_count, source_file, description = meta
            if description:
                lines.append(f"{description}")
                lines.append("")
            if source_file:
                lines.append(f"Source file: `{source_file}`")
            if row_count:
                lines.append(f"Rows: {row_count:,}")
            if source_file or row_count:
                lines.append("")

        lines.append("| Column | Type | Nulls | Example | Join |")
        lines.append("|--------|------|-------|---------|------|")

        cols = con.execute(
            "SELECT column_name, data_type, null_pct, example_value, join_hint "
            "FROM _columns WHERE table_name = ? ORDER BY rowid",
            [table_name],
        ).fetchall()

        for col_name, dtype, null_pct, example, join_hint in cols:
            null_str = f"{null_pct:.1f}%" if null_pct is not None else ""
            example_str = (example or "").replace("|", "\\|")
            join_str = join_hint or ""
            lines.append(
                f"| {col_name} | {dtype} | {null_str} | {example_str} | {join_str} |"
            )

        lines.append("")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))
    print(f"  Exported to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Build DuckDB from AACT ClinicalTrials.gov flat files"
    )
    parser.add_argument(
        "--zip", type=Path, default=None,
        help="Path to an already-downloaded AACT zip file",
    )
    parser.add_argument(
        "--data-dir", type=Path, default=None,
        help="Path to already-extracted .txt files",
    )
    parser.add_argument(
        "--output", type=Path, default=Path("clinicaltrials.duckdb"),
        help="Output database path (default: clinicaltrials.duckdb)",
    )
    parser.add_argument(
        "--tables", nargs="+", default=None,
        help="Build only specific tables (by table name)",
    )
    args = parser.parse_args()

    t_start = time.time()
    print("Building ClinicalTrials.gov database from AACT flat files\n")

    # -----------------------------------------------------------------------
    # Step 1: Get the data files
    # -----------------------------------------------------------------------
    print("[1/7] Acquiring data files")

    if args.data_dir and args.data_dir.exists():
        txt_files = discover_txt_files(args.data_dir)
        print(f"  Found {len(txt_files)} .txt files in {args.data_dir}")
    elif args.zip and args.zip.exists():
        print(f"  Extracting {args.zip}")
        data_dir = Path("aact_data")
        txt_files = extract_zip(args.zip, data_dir)
    else:
        # Download from AACT
        url = find_download_url()
        if not url:
            print("  ERROR: Could not find download URL on AACT page.")
            print("  Try downloading manually and use --zip or --data-dir.")
            sys.exit(1)

        zip_path = Path("aact_export.zip")
        download_zip(url, zip_path)

        print("  Extracting zip file...")
        data_dir = Path("aact_data")
        txt_files = extract_zip(zip_path, data_dir)

    if not txt_files:
        print("  ERROR: No .txt files found.")
        sys.exit(1)

    print(f"  {len(txt_files)} tables to load")

    # -----------------------------------------------------------------------
    # Step 2: Load tables into DuckDB
    # -----------------------------------------------------------------------
    print(f"\n[2/7] Loading tables into DuckDB")

    db_path = args.output
    db_path.unlink(missing_ok=True)
    con = duckdb.connect(str(db_path))

    built_tables = set()
    file_map = {}

    # Build list of files to load
    files_to_load = []
    for filepath in txt_files:
        table_name = table_name_from_file(filepath)
        if args.tables and table_name not in args.tables:
            continue
        files_to_load.append((table_name, filepath))

    for table_name, filepath in sorted(files_to_load):
        t0 = time.time()
        row_count = load_table(con, table_name, filepath)
        elapsed = time.time() - t0

        if row_count > 0:
            built_tables.add(table_name)
            file_map[table_name] = filepath.name
            print(f"  {table_name:<35s} {row_count:>12,} rows  ({elapsed:.1f}s)")
        else:
            print(f"  {table_name:<35s} SKIPPED (empty or error)")

    # Drop any tables that loaded with 0 rows (e.g. search_results)
    all_tables_check = list(built_tables)
    for table_name in all_tables_check:
        rc = con.execute(f'SELECT COUNT(*) FROM "{table_name}"').fetchone()[0]
        if rc == 0:
            con.execute(f'DROP TABLE IF EXISTS "{table_name}"')
            built_tables.discard(table_name)
            file_map.pop(table_name, None)

    print(f"\n  Loaded {len(built_tables)} tables")

    # -----------------------------------------------------------------------
    # Step 3: Cast date columns
    # -----------------------------------------------------------------------
    print(f"\n[3/7] Casting date columns")

    for table_name in sorted(built_tables):
        try:
            cast_date_columns(con, table_name)
        except Exception as e:
            print(f"  WARNING: casting {table_name}: {e}")

    print("  Done")

    # -----------------------------------------------------------------------
    # Step 4: Check for expected tables
    # -----------------------------------------------------------------------
    print(f"\n[4/7] Checking expected tables")

    missing = [t for t in EXPECTED_TABLES if t not in built_tables]
    if missing:
        print(f"  WARNING: Missing expected tables: {', '.join(missing)}")
    else:
        print(f"  All {len(EXPECTED_TABLES)} expected tables present")

    # -----------------------------------------------------------------------
    # Step 5: Build metadata
    # -----------------------------------------------------------------------
    print(f"\n[5/7] Building metadata")

    build_metadata(con, built_tables, file_map)
    meta_count = con.execute("SELECT COUNT(*) FROM _metadata").fetchone()[0]
    print(f"  {meta_count} tables cataloged in _metadata")

    # -----------------------------------------------------------------------
    # Step 6: Build _columns data dictionary
    # -----------------------------------------------------------------------
    print(f"\n[6/7] Building _columns data dictionary")

    build_columns_table(con)
    col_count = con.execute("SELECT COUNT(*) FROM _columns").fetchone()[0]
    print(f"  {col_count} columns cataloged in _columns")

    # -----------------------------------------------------------------------
    # Step 7: Export DICTIONARY.md
    # -----------------------------------------------------------------------
    print(f"\n[7/7] Exporting DICTIONARY.md")

    export_dictionary(con, db_path.parent / "DICTIONARY.md")

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    total_rows = con.execute(
        "SELECT SUM(row_count) FROM _metadata"
    ).fetchone()[0]

    con.close()

    db_size = db_path.stat().st_size / (1024**3)
    elapsed_total = time.time() - t_start
    minutes = int(elapsed_total // 60)
    seconds = int(elapsed_total % 60)

    print(f"\nDone in {minutes}m {seconds}s")
    print(f"Database: {db_path.resolve()}")
    print(f"Size: {db_size:.2f} GB")
    print(f"Tables: {len(built_tables)}")
    print(f"Total rows: {total_rows:,}")


if __name__ == "__main__":
    main()
