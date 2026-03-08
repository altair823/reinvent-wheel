SHELL := /bin/bash
REPO_ROOT := $(abspath ../../..)
.PHONY: build run test e2e smoke

build:
	bash -lc "source '$(REPO_ROOT)/scripts/env.sh' && cargo build --manifest-path Cargo.toml"

run:
	bash -lc "source '$(REPO_ROOT)/scripts/env.sh' && cargo run --manifest-path Cargo.toml -- ../fixtures/sample.json"

test:
	bash -lc "source '$(REPO_ROOT)/scripts/env.sh' && cargo test --manifest-path Cargo.toml"

e2e:
	bash ../e2e/rust-smoke.sh

smoke:
	$(MAKE) run
