#!/usr/bin/env bash
set -euo pipefail

# rebuild_and_publish.sh — ClinicalTrials.gov Database
# Usage: cd ~/clinicaltrials-database && bash scripts/rebuild_and_publish.sh

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

# AACT downloads page — we discover the actual file URL dynamically
AACT_DOWNLOADS_PAGE="https://aact.ctti-clinicaltrials.org/pipe_files"
HF_REPO="Nason/clinicaltrials-database"
LAST_MOD_FILE="data/.last_modified"
LOG_DIR="logs"

# --- Preflight ---
if [[ -z "${HF_TOKEN:-}" ]]; then
    echo "ERROR: HF_TOKEN environment variable is required."
    exit 1
fi

mkdir -p "$LOG_DIR" data
LOGFILE="$LOG_DIR/rebuild_$(date +%Y-%m-%d).log"
exec > >(tee -a "$LOGFILE") 2>&1
echo "=== ClinicalTrials rebuild started at $(date) ==="

# --- Discover the AACT flat file URL ---
echo "Checking for updates..."
SOURCE_URL=$(curl -sL "$AACT_DOWNLOADS_PAGE" | grep -oP 'href="\Khttps://[^"]*export_ctgov[^"]*' | head -1 || true)

if [[ -z "$SOURCE_URL" ]]; then
    # Fallback: let build_database.py find the URL itself
    echo "WARNING: Could not discover AACT URL from downloads page. Will rebuild unconditionally."
    REMOTE_MOD=""
else
    REMOTE_MOD=$(curl -sI "$SOURCE_URL" | grep -i "^last-modified:" | sed 's/^[Ll]ast-[Mm]odified: //' | tr -d '\r')
fi

if [[ -z "$REMOTE_MOD" ]]; then
    echo "WARNING: Could not get Last-Modified header. Proceeding with rebuild."
elif [[ -f "$LAST_MOD_FILE" ]]; then
    LOCAL_MOD=$(cat "$LAST_MOD_FILE")
    if [[ "$REMOTE_MOD" == "$LOCAL_MOD" ]]; then
        echo "No update available (Last-Modified: $REMOTE_MOD)."
        echo "=== ClinicalTrials rebuild finished at $(date) ==="
        exit 0
    fi
    echo "New data found (remote: $REMOTE_MOD, local: $LOCAL_MOD)."
else
    echo "No previous build timestamp found. Proceeding with rebuild."
fi

# --- Rebuild ---
echo "New data found, rebuilding..."

echo "[1/3] Building database..."
uv run python build_database.py

echo "[2/3] Validating database..."
uv run python validate_database.py

echo "[3/3] Uploading to Hugging Face..."
uv run python publish_to_hf.py --repo "$HF_REPO" --token "$HF_TOKEN"

# --- Save timestamp ---
if [[ -n "${REMOTE_MOD:-}" ]]; then
    echo "$REMOTE_MOD" > "$LAST_MOD_FILE"
fi

echo "Upload complete."
echo "=== ClinicalTrials rebuild finished at $(date) ==="
