SHELL := /bin/bash
REPO_ROOT := $(abspath ../../..)
PROJECT_PATH := :t16-notes-app-jvm-kotlin
.PHONY: build run test e2e smoke

build:
	bash -lc "cd '$(REPO_ROOT)' && ./gradlew $(PROJECT_PATH):installDist"

run:
	bash -lc "cd '$(REPO_ROOT)' && ./gradlew -q $(PROJECT_PATH):run --args='../fixtures/notes.txt'"

test:
	bash -lc "cd '$(REPO_ROOT)' && ./gradlew $(PROJECT_PATH):test"

e2e:
	bash ../e2e/kotlin-smoke.sh

smoke:
	$(MAKE) run
