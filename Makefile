SHELL := /bin/bash
.PHONY: bootstrap verify smoke list clean

bootstrap:
	./scripts/bootstrap-rust.sh
	./scripts/bootstrap-jdk.sh
	./scripts/bootstrap-gradle.sh
	./scripts/bootstrap-python.sh

verify:
	./scripts/verify-all.sh

smoke:
	./scripts/smoke-all.sh

list:
	./scripts/list-projects.py

clean:
	rm -rf .toolchains .venv artifacts
	find topics -type d \( -name target -o -name build -o -name bin -o -name __pycache__ \) -prune -exec rm -rf {} +
