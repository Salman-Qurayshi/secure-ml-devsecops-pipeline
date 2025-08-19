#!/usr/bin/env bash
set -euo pipefail

IMAGE="${1:-}"
if [ -z "$IMAGE" ]; then
  echo "Usage: $0 <image:tag>"
  exit 2
fi

mkdir -p ci-cd
# SBOM doesn’t fail the build; it’s an artifact you can sign/attest later
syft packages "$IMAGE" -o json > ci-cd/sbom.json
echo "SBOM generated at ci-cd/sbom.json"
