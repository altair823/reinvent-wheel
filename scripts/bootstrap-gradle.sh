#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$REPO_ROOT/scripts/env.sh"
mkdir -p "$TOOLCHAINS_DIR"
if [ -x "$GRADLE_HOME/bin/gradle" ]; then
  exit 0
fi
archive="$TOOLCHAINS_DIR/gradle-$GRADLE_VERSION-bin.zip"
curl -fL "$GRADLE_DOWNLOAD_URL" -o "$archive"
"$PYTHON_BIN" - "$archive" "$TOOLCHAINS_DIR" <<'PY'
import sys
import zipfile
from pathlib import Path
archive = Path(sys.argv[1])
out_dir = Path(sys.argv[2])
with zipfile.ZipFile(archive) as zf:
    zf.extractall(out_dir)
PY
chmod +x "$GRADLE_HOME/bin/gradle"
