#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
pushd "$ROOT/cpp" >/dev/null
make -s --no-print-directory run > /tmp/file-log-library-cpp-out.txt
if ! diff -u "$ROOT/fixtures/mission-expected.txt" /tmp/file-log-library-cpp-out.txt; then
  echo "Mission not complete for C++: implement the topic until stdout matches fixtures/mission-expected.txt" >&2
  exit 1
fi
popd >/dev/null
