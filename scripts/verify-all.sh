#!/usr/bin/env bash
set -uo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$REPO_ROOT/scripts/env.sh"
LOG_DIR="$REPO_ROOT/artifacts/verify"
SUMMARY="$LOG_DIR/summary.txt"
STATUS=0
mkdir -p "$LOG_DIR"
: > "$SUMMARY"

TEMPLATE_PASS=0
TEMPLATE_FAIL=0
TEMPLATE_SKIP=0
TEST_PASS=0
TEST_FAIL=0
TEST_SKIP=0
MISSION_PASS=0
MISSION_FAIL=0
MISSION_SKIP=0

add_result() {
  local phase="$1"
  local result="$2"
  case "$phase:$result" in
    template:PASS) TEMPLATE_PASS=$((TEMPLATE_PASS + 1)) ;;
    template:FAIL) TEMPLATE_FAIL=$((TEMPLATE_FAIL + 1)) ;;
    template:SKIP) TEMPLATE_SKIP=$((TEMPLATE_SKIP + 1)) ;;
    test:PASS) TEST_PASS=$((TEST_PASS + 1)) ;;
    test:FAIL) TEST_FAIL=$((TEST_FAIL + 1)) ;;
    test:SKIP) TEST_SKIP=$((TEST_SKIP + 1)) ;;
    mission:PASS) MISSION_PASS=$((MISSION_PASS + 1)) ;;
    mission:FAIL) MISSION_FAIL=$((MISSION_FAIL + 1)) ;;
    mission:SKIP) MISSION_SKIP=$((MISSION_SKIP + 1)) ;;
  esac
}

print_phase_header() {
  local phase="$1"
  local label="$2"
  echo
  echo "## $label"
  echo "## $label" >> "$SUMMARY"
}

run_step() {
  local phase="$1"
  local name="$2"
  local log_path="$3"
  shift 3
  echo "== [$phase] $name =="
  if "$@" >"$log_path" 2>&1; then
    echo "PASS [$phase] $name" | tee -a "$SUMMARY"
    add_result "$phase" "PASS"
  else
    local rc=$?
    echo "FAIL [$phase] $name (exit=$rc)" | tee -a "$SUMMARY"
    add_result "$phase" "FAIL"
    STATUS=1
  fi
}

skip_step() {
  local phase="$1"
  local name="$2"
  echo "SKIP [$phase] $name" | tee -a "$SUMMARY"
  add_result "$phase" "SKIP"
}

print_phase_totals() {
  local phase="$1"
  case "$phase" in
    template)
      echo "TOTAL [$phase] pass=$TEMPLATE_PASS fail=$TEMPLATE_FAIL skip=$TEMPLATE_SKIP" | tee -a "$SUMMARY"
      ;;
    test)
      echo "TOTAL [$phase] pass=$TEST_PASS fail=$TEST_FAIL skip=$TEST_SKIP" | tee -a "$SUMMARY"
      ;;
    mission)
      echo "TOTAL [$phase] pass=$MISSION_PASS fail=$MISSION_FAIL skip=$MISSION_SKIP" | tee -a "$SUMMARY"
      ;;
  esac
}

print_phase_header "template" "Template Health"
while IFS= read -r project; do
  run_step "template" "$project:smoke" "$LOG_DIR/template__$(echo "$project" | tr '/ ' '__').log" make -C "$REPO_ROOT/$project" smoke
done < <("$REPO_ROOT/scripts/list-projects.py")
print_phase_totals "template"

print_phase_header "test" "Project Tests"
while IFS= read -r project; do
  run_step "test" "$project:test" "$LOG_DIR/test__$(echo "$project" | tr '/ ' '__').log" make -C "$REPO_ROOT/$project" test
done < <("$REPO_ROOT/scripts/list-projects.py")
print_phase_totals "test"

print_phase_header "mission" "Mission E2E"
while IFS= read -r script; do
  run_step "mission" "${script#"$REPO_ROOT/"}" "$LOG_DIR/mission__$(echo "${script#"$REPO_ROOT/topics/"}" | tr '/ ' '__').log" bash "$script"
done < <(find "$REPO_ROOT/topics" -path '*/e2e/*.sh' | sort)
print_phase_totals "mission"

echo | tee -a "$SUMMARY"
echo "OVERALL STATUS: $([ "$STATUS" -eq 0 ] && echo PASS || echo FAIL)" | tee -a "$SUMMARY"
echo
cat "$SUMMARY"
exit "$STATUS"
