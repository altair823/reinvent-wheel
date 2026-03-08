#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
pushd "$ROOT/java" >/dev/null
make -s --no-print-directory run > /tmp/rate-limiter-java-out.txt
if ! diff -u "$ROOT/fixtures/mission-expected.txt" /tmp/rate-limiter-java-out.txt; then
  echo "Mission not complete for Java: implement the topic until stdout matches fixtures/mission-expected.txt" >&2
  exit 1
fi
popd >/dev/null
