#!/usr/bin/env bash
set -euo pipefail

REQ="${1:-requirements.txt}"
mkdir -p ci-cd

# pip-audit exits nonzero if vulns found; that's what we want
python -m pip install --upgrade pip >/dev/null
python -m pip install pip-audit >/dev/null

pip-audit -r "$REQ" --format json -o ci-cd/pip-audit.json
echo "Dependency scan complete."
