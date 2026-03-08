#!/usr/bin/env bash
set -euo pipefail
MODE="${1:-mission}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOPIC_NAME="${ROOT##*/}"
SCRIPT_NAME="${BASH_SOURCE[0]##*/}"
LANGUAGE="${SCRIPT_NAME%-smoke.sh}"
PORT="${PORT:-18082}"
export PORT
pushd "$ROOT/kotlin" >/dev/null
make -s --no-print-directory run > /tmp/http-server-router-kotlin.log 2>&1 &
pid=$!
trap 'kill $pid 2>/dev/null || true; wait $pid 2>/dev/null || true' EXIT
for _ in $(seq 1 160); do
  if curl -fsS "http://127.0.0.1:$PORT/health" > /tmp/http-server-router-kotlin-health.txt 2>/dev/null; then
    break
  fi
  sleep 0.25
done
curl -fsS -X POST --data-binary @"$ROOT/fixtures/echo-body.txt" "http://127.0.0.1:$PORT/echo" > /tmp/http-server-router-kotlin-echo.txt
diff -u "$ROOT/fixtures/expected-health.txt" /tmp/http-server-router-kotlin-health.txt
diff -u "$ROOT/fixtures/expected-echo.txt" /tmp/http-server-router-kotlin-echo.txt
if [ "$MODE" = "mission" ]; then
  status_404="$(curl -s -o /tmp/http-server-router-kotlin-404.txt -w '%{http_code}' "http://127.0.0.1:$PORT/missing")"
  if [ "$status_404" != "404" ]; then
    echo "Mission not complete: expected 404 for unknown route, got $status_404" >&2
    exit 1
  fi
  status_405="$(curl -s -o /tmp/http-server-router-kotlin-405.txt -w '%{http_code}' "http://127.0.0.1:$PORT/echo")"
  if [ "$status_405" != "405" ]; then
    echo "Mission not complete: expected 405 for GET /echo, got $status_405" >&2
    exit 1
  fi
fi
echo "E2E PASS: $TOPIC_NAME ($LANGUAGE, mode=$MODE)"
popd >/dev/null
