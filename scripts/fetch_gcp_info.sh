#!/usr/bin/env bash
# Fetch basic GCP information using gcloud and store it as JSON.
# Usage: ./scripts/fetch_gcp_info.sh [output-file]

set -euo pipefail

OUT_FILE="${1:-gcp-info.json}"

# Ensure gcloud is initialized and authenticated before running.

tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT

# Query projects and billing accounts
projects_file="$tmpdir/projects.json"
billing_file="$tmpdir/billing.json"

gcloud projects list --format=json > "$projects_file"
gcloud billing accounts list --format=json > "$billing_file"

# Combine results into a single JSON file
jq -n \
  --slurpfile projects "$projects_file" \
  --slurpfile billing "$billing_file" \
  '{projects: $projects[0], billing_accounts: $billing[0]}' \
  > "$OUT_FILE"

echo "GCP information written to $OUT_FILE"
