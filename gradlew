#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$REPO_ROOT/scripts/env.sh"
if [ -z "${GRADLE_BIN:-}" ] || [ ! -x "$GRADLE_BIN" ]; then
  echo "Gradle is not bootstrapped. Run make bootstrap first." >&2
  exit 1
fi
exec "$GRADLE_BIN" "$@"
