#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOPIC_NAME="${ROOT##*/}"
SCRIPT_NAME="${BASH_SOURCE[0]##*/}"
LANGUAGE="${SCRIPT_NAME%-smoke.sh}"
pushd "$ROOT/python" >/dev/null
make -s --no-print-directory run > /tmp/external-sort-merge-python-out.txt
if ! diff -u "$ROOT/fixtures/mission-expected.txt" /tmp/external-sort-merge-python-out.txt; then
  echo "Mission not complete for Python: implement the topic until stdout matches fixtures/mission-expected.txt" >&2
  exit 1
fi
echo "E2E PASS: $TOPIC_NAME ($LANGUAGE)"
popd >/dev/null
