#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# shellcheck disable=SC1091
source "$REPO_ROOT/toolchains/versions.env"
export TOOLCHAINS_DIR="$REPO_ROOT/.toolchains"
export CARGO_HOME="$TOOLCHAINS_DIR/cargo"
export RUSTUP_HOME="$TOOLCHAINS_DIR/rustup"
export PYTHON_HOME="$TOOLCHAINS_DIR/python-$PYTHON_VERSION"
export JAVA_HOME="$TOOLCHAINS_DIR/jdk-$JAVA_VERSION"
export GRADLE_HOME="$TOOLCHAINS_DIR/gradle-$GRADLE_VERSION"
export GRADLE_USER_HOME="$REPO_ROOT/.gradle-home"
if [ -x "$PYTHON_HOME/bin/python3" ]; then
  export PYTHON_BIN="$PYTHON_HOME/bin/python3"
else
  export PYTHON_BIN="$(command -v python3)"
fi
if [ -x "$CARGO_HOME/bin/cargo" ]; then
  export PATH="$CARGO_HOME/bin:$PATH"
fi
if [ -x "$JAVA_HOME/bin/java" ]; then
  export PATH="$JAVA_HOME/bin:$PATH"
fi
if [ -f "$GRADLE_HOME/bin/gradle" ]; then
  export GRADLE_BIN="$GRADLE_HOME/bin/gradle"
fi
export VIRTUAL_ENV="$REPO_ROOT/.venv"
if [ -d "$VIRTUAL_ENV/bin" ]; then
  export PATH="$VIRTUAL_ENV/bin:$PATH"
fi
