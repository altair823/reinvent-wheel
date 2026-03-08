#!/usr/bin/env bash
set -uo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="$REPO_ROOT/artifacts/smoke"
SUMMARY="$LOG_DIR/summary.txt"
STATUS=0
mkdir -p "$LOG_DIR"
: > "$SUMMARY"

run_step() {
  local name="$1"
  local log_path="$2"
  shift 2
  echo "== $name =="
  if "$@" >"$log_path" 2>&1; then
    echo "PASS $name" | tee -a "$SUMMARY"
  else
    local rc=$?
    echo "FAIL $name (exit=$rc)" | tee -a "$SUMMARY"
    STATUS=1
  fi
}

while IFS= read -r project; do
  run_step "$project:smoke" "$LOG_DIR/$(echo "$project" | tr '/ ' '__').log" make -C "$REPO_ROOT/$project" smoke
done < <("$REPO_ROOT/scripts/list-projects.py")
echo
cat "$SUMMARY"
exit "$STATUS"
