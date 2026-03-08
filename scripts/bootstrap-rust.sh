#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$REPO_ROOT/scripts/env.sh"
mkdir -p "$TOOLCHAINS_DIR"
if [ -x "$CARGO_HOME/bin/cargo" ] && "$CARGO_HOME/bin/rustc" --version | grep -q "$RUST_VERSION"; then
  exit 0
fi
curl -fsSL "$RUSTUP_INIT_URL" -o "$TOOLCHAINS_DIR/rustup-init.sh"
chmod +x "$TOOLCHAINS_DIR/rustup-init.sh"
CARGO_HOME="$CARGO_HOME" RUSTUP_HOME="$RUSTUP_HOME" "$TOOLCHAINS_DIR/rustup-init.sh" -y --profile minimal --default-toolchain "$RUST_VERSION" --no-modify-path
