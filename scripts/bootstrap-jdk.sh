#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$REPO_ROOT/scripts/env.sh"
mkdir -p "$TOOLCHAINS_DIR"
if [ -x "$JAVA_HOME/bin/java" ] && "$JAVA_HOME/bin/java" -version 2>&1 | grep -q "$JAVA_VERSION"; then
  exit 0
fi
archive="$TOOLCHAINS_DIR/jdk-$JAVA_VERSION.tar.gz"
tmp="$TOOLCHAINS_DIR/jdk-extract"
rm -rf "$JAVA_HOME" "$tmp"
curl -fL "$JAVA_DOWNLOAD_URL" -o "$archive"
mkdir -p "$tmp"
tar -xzf "$archive" -C "$tmp"
mv "$(find "$tmp" -mindepth 1 -maxdepth 1 -type d | head -n 1)" "$JAVA_HOME"
rm -rf "$tmp"
