SHELL := /bin/bash
REPO_ROOT := $(abspath ../../..)
.PHONY: run test e2e smoke

run:
	bash -lc 'source "$(REPO_ROOT)/scripts/env.sh" && export PYTHONPATH="$(CURDIR)/src" && "$$PYTHON_BIN" -m t22_external_sort_merge_python.cli ../fixtures/numbers.txt'

test:
	bash -lc 'source "$(REPO_ROOT)/scripts/env.sh" && export PYTHONPATH="$(CURDIR)/src" && "$$PYTHON_BIN" -m unittest discover -s tests'

e2e:
	bash ../e2e/python-smoke.sh

smoke:
	$(MAKE) run
