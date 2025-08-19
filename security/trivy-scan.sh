#!/usr/bin/env bash
set -euo pipefail

IMAGE="${1:-}"
if [ -z "$IMAGE" ]; then
  echo "Usage: $0 <image:tag>"
  exit 2
fi

mkdir -p ci-cd

# Fail the build on HIGH/CRITICAL vulns
trivy image --quiet \
  --severity HIGH,CRITICAL \
  --exit-code 1 \
  --format table \
  --output ci-cd/trivy-report.txt \
  "$IMAGE"

# Also keep a JSON artifact
trivy image --quiet \
  --severity HIGH,CRITICAL \
  --format json \
  --output ci-cd/trivy-report.json \
  "$IMAGE"

echo "Trivy scan complete."
