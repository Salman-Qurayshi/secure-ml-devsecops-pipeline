#!/usr/bin/env bash
set -euo pipefail
mkdir -p ci-cd
# Run the official Docker Bench. This does NOT fail the build (advisory).
docker run --rm --net host --pid host \
  --cap-add audit_control -e DOCKER_CONTENT_TRUST=1 \
  -v /etc:/etc:ro -v /usr/bin/docker-containerd:/usr/bin/docker-containerd:ro \
  -v /usr/lib/systemd:/usr/lib/systemd:ro -v /var/lib:/var/lib:ro \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -v /usr/bin/containerd:/usr/bin/containerd:ro \
  docker/docker-bench-security > ci-cd/docker-bench.txt || true
echo "Docker Bench complete (advisory)."
