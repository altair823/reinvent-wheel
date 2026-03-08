#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
pushd "$ROOT/rust" >/dev/null
make -s --no-print-directory run > /tmp/mini-git-object-store-rust-out.txt
if ! diff -u "$ROOT/fixtures/mission-expected.txt" /tmp/mini-git-object-store-rust-out.txt; then
  echo "Mission not complete for Rust: implement the topic until stdout matches fixtures/mission-expected.txt" >&2
  exit 1
fi
popd >/dev/null
