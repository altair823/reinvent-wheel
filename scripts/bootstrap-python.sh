#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$REPO_ROOT/scripts/env.sh"
mkdir -p "$TOOLCHAINS_DIR"
if [ ! -x "$PYTHON_HOME/bin/python3" ]; then
  archive="$TOOLCHAINS_DIR/Python-$PYTHON_VERSION.tgz"
  build_dir="$TOOLCHAINS_DIR/python-build"
  rm -rf "$build_dir"
  curl -fL "$PYTHON_SOURCE_URL" -o "$archive"
  mkdir -p "$build_dir"
  tar -xzf "$archive" -C "$build_dir"
  cd "$(find "$build_dir" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
  ./configure --prefix="$PYTHON_HOME" --without-ensurepip
  make -j"$(nproc)"
  make install
fi
rm -rf "$REPO_ROOT/.venv"
"$PYTHON_HOME/bin/python3" -m venv --without-pip "$REPO_ROOT/.venv"
if "$PYTHON_HOME/bin/python3" -c "import ssl, zlib" >/dev/null 2>&1; then
  "$REPO_ROOT/.venv/bin/python" -m ensurepip --upgrade
  "$REPO_ROOT/.venv/bin/pip" install --upgrade pip
  "$REPO_ROOT/.venv/bin/pip" install duckdb
else
  echo "Python $PYTHON_VERSION is available but lacks ssl/zlib; created a venv without pip." >&2
fi
