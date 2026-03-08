#!/usr/bin/env python3
from __future__ import annotations

import stat
from pathlib import Path

from scaffold_catalog import (
    ROOT,
    TOPICS,
    argv_contract,
    class_name,
    direct_commands_for,
    fixtures_for,
    gradle_path,
    hello_output,
    java_package,
    language_write_hint,
    project_name,
    render_hand_coding_topics,
    render_root_readme,
    render_topic_qa,
    render_topic_readme,
    render_topic_spec,
    text,
    topic_language_commands,
    topic_language_files,
    topic_dir,
)
from scaffold_cpp_projects import render_cpp_e2e, render_cpp_header, render_cpp_lib, render_cpp_main, render_cpp_makefile, render_cpp_test
from scaffold_jvm_projects import (
    render_java_build_gradle,
    render_java_e2e,
    render_java_makefile,
    render_java_source,
    render_java_test,
    render_kotlin_build_gradle,
    render_kotlin_e2e,
    render_kotlin_makefile,
    render_kotlin_source,
    render_kotlin_test,
)
from scaffold_python_projects import render_python_cli, render_python_core, render_python_e2e, render_python_makefile, render_python_pyproject, render_python_test
from scaffold_rust_projects import render_rust_cargo_toml, render_rust_e2e, render_rust_makefile, render_rust_test, rust_lib_code, rust_main_code


def write(path: Path, content: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    if executable:
        path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def render_root_makefile() -> str:
    return text(
        """
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
        	find topics -type d \\( -name target -o -name build -o -name bin -o -name __pycache__ \\) -prune -exec rm -rf {} +
        """
    )


def render_gitignore() -> str:
    return text(
        """
        # Local toolchains and environments
        .toolchains/
        .venv/
        .python-version

        # Build and cache directories
        .gradle/
        .gradle-home/
        artifacts/
        .cache/
        .pytest_cache/
        .mypy_cache/
        .ruff_cache/
        **/target/
        **/build/
        **/bin/
        **/__pycache__/

        # IDE and OS files
        .idea/
        .vscode/
        .DS_Store
        Thumbs.db

        # Coverage and runtime outputs
        .coverage
        coverage/
        *.class
        *.log
        *.db
        *.sqlite
        *.sqlite3
        *.pyc
        *.pyo
        *.tmp
        *.swp
        *.swo
        *.out
        """
    )


def render_versions_env() -> str:
    return text(
        """
        RUST_VERSION=1.94.0
        PYTHON_VERSION=3.14.3
        JAVA_VERSION=25.0.2
        GRADLE_VERSION=9.4.0
        KOTLIN_VERSION=2.3.10
        CXX_STANDARD=c++23
        RUSTUP_INIT_URL=https://sh.rustup.rs
        PYTHON_SOURCE_URL=https://www.python.org/ftp/python/3.14.3/Python-3.14.3.tgz
        JAVA_DOWNLOAD_URL=https://download.oracle.com/java/25/archive/jdk-25.0.2_linux-x64_bin.tar.gz
        GRADLE_DOWNLOAD_URL=https://services.gradle.org/distributions/gradle-9.4.0-bin.zip
        """
    )


def render_env_sh() -> str:
    return text(
        """
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
        """
    )


def render_bootstrap_rust() -> str:
    return text(
        """
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
        """
    )


def render_bootstrap_jdk() -> str:
    return text(
        """
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
        """
    )


def render_bootstrap_gradle() -> str:
    return text(
        """
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
        """
    )


def render_bootstrap_python() -> str:
    return text(
        """
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
        """
    )


def render_list_projects() -> str:
    return text(
        """
        #!/usr/bin/env python3
        from pathlib import Path
        root = Path(__file__).resolve().parent.parent / "topics"
        for makefile in sorted(root.glob("*/**/Makefile")):
            print(makefile.parent.relative_to(root.parent))
        """
    )


def render_verify_all() -> str:
    return text(
        """
        #!/usr/bin/env bash
        set -uo pipefail
        REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
        source "$REPO_ROOT/scripts/env.sh"
        LOG_DIR="$REPO_ROOT/artifacts/verify"
        SUMMARY="$LOG_DIR/summary.txt"
        STATUS=0
        mkdir -p "$LOG_DIR"
        : > "$SUMMARY"

        TEMPLATE_PASS=0
        TEMPLATE_FAIL=0
        TEMPLATE_SKIP=0
        TEST_PASS=0
        TEST_FAIL=0
        TEST_SKIP=0
        MISSION_PASS=0
        MISSION_FAIL=0
        MISSION_SKIP=0

        add_result() {
          local phase="$1"
          local result="$2"
          case "$phase:$result" in
            template:PASS) TEMPLATE_PASS=$((TEMPLATE_PASS + 1)) ;;
            template:FAIL) TEMPLATE_FAIL=$((TEMPLATE_FAIL + 1)) ;;
            template:SKIP) TEMPLATE_SKIP=$((TEMPLATE_SKIP + 1)) ;;
            test:PASS) TEST_PASS=$((TEST_PASS + 1)) ;;
            test:FAIL) TEST_FAIL=$((TEST_FAIL + 1)) ;;
            test:SKIP) TEST_SKIP=$((TEST_SKIP + 1)) ;;
            mission:PASS) MISSION_PASS=$((MISSION_PASS + 1)) ;;
            mission:FAIL) MISSION_FAIL=$((MISSION_FAIL + 1)) ;;
            mission:SKIP) MISSION_SKIP=$((MISSION_SKIP + 1)) ;;
          esac
        }

        print_phase_header() {
          local phase="$1"
          local label="$2"
          echo
          echo "## $label"
          echo "## $label" >> "$SUMMARY"
        }

        run_step() {
          local phase="$1"
          local name="$2"
          local log_path="$3"
          shift 3
          echo "== [$phase] $name =="
          if "$@" >"$log_path" 2>&1; then
            echo "PASS [$phase] $name" | tee -a "$SUMMARY"
            add_result "$phase" "PASS"
          else
            local rc=$?
            echo "FAIL [$phase] $name (exit=$rc)" | tee -a "$SUMMARY"
            add_result "$phase" "FAIL"
            STATUS=1
          fi
        }

        skip_step() {
          local phase="$1"
          local name="$2"
          echo "SKIP [$phase] $name" | tee -a "$SUMMARY"
          add_result "$phase" "SKIP"
        }

        print_phase_totals() {
          local phase="$1"
          case "$phase" in
            template)
              echo "TOTAL [$phase] pass=$TEMPLATE_PASS fail=$TEMPLATE_FAIL skip=$TEMPLATE_SKIP" | tee -a "$SUMMARY"
              ;;
            test)
              echo "TOTAL [$phase] pass=$TEST_PASS fail=$TEST_FAIL skip=$TEST_SKIP" | tee -a "$SUMMARY"
              ;;
            mission)
              echo "TOTAL [$phase] pass=$MISSION_PASS fail=$MISSION_FAIL skip=$MISSION_SKIP" | tee -a "$SUMMARY"
              ;;
          esac
        }

        print_phase_header "template" "Template Health"
        while IFS= read -r project; do
          run_step "template" "$project:smoke" "$LOG_DIR/template__$(echo "$project" | tr '/ ' '__').log" make -C "$REPO_ROOT/$project" smoke
        done < <("$REPO_ROOT/scripts/list-projects.py")
        print_phase_totals "template"

        print_phase_header "test" "Project Tests"
        while IFS= read -r project; do
          run_step "test" "$project:test" "$LOG_DIR/test__$(echo "$project" | tr '/ ' '__').log" make -C "$REPO_ROOT/$project" test
        done < <("$REPO_ROOT/scripts/list-projects.py")
        print_phase_totals "test"

        print_phase_header "mission" "Mission E2E"
        while IFS= read -r script; do
          run_step "mission" "${script#"$REPO_ROOT/"}" "$LOG_DIR/mission__$(echo "${script#"$REPO_ROOT/topics/"}" | tr '/ ' '__').log" bash "$script"
        done < <(find "$REPO_ROOT/topics" -path '*/e2e/*.sh' | sort)
        print_phase_totals "mission"

        echo | tee -a "$SUMMARY"
        echo "OVERALL STATUS: $([ "$STATUS" -eq 0 ] && echo PASS || echo FAIL)" | tee -a "$SUMMARY"
        echo
        cat "$SUMMARY"
        exit "$STATUS"
        """
    )


def render_smoke_all() -> str:
    return text(
        """
        #!/usr/bin/env bash
        set -uo pipefail
        REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
        LOG_DIR="$REPO_ROOT/artifacts/smoke"
        SUMMARY="$LOG_DIR/summary.txt"
        STATUS=0
        mkdir -p "$LOG_DIR"
        : > "$SUMMARY"

        run_step() {
          local name="$1"
          local log_path="$2"
          shift 2
          echo "== $name =="
          if "$@" >"$log_path" 2>&1; then
            echo "PASS $name" | tee -a "$SUMMARY"
          else
            local rc=$?
            echo "FAIL $name (exit=$rc)" | tee -a "$SUMMARY"
            STATUS=1
          fi
        }

        while IFS= read -r project; do
          run_step "$project:smoke" "$LOG_DIR/$(echo "$project" | tr '/ ' '__').log" make -C "$REPO_ROOT/$project" smoke
        done < <("$REPO_ROOT/scripts/list-projects.py")
        echo
        cat "$SUMMARY"
        exit "$STATUS"
        """
    )


def render_cargo_toml() -> str:
    members = ",\n".join(f'"topics/{topic["num"]:02d}-{topic["slug"]}/rust"' for topic in TOPICS if "rust" in topic["languages"])
    return text(
        f"""
        [workspace]
        members = [
        {members}
        ]
        resolver = "2"
        """
    )


def render_settings_gradle() -> str:
    lines = [
        'rootProject.name = "hand-coding-wheel"',
        "",
        "dependencyResolutionManagement {",
        "    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)",
        "    repositories {",
        "        mavenCentral()",
        "    }",
        "}",
        "",
        "pluginManagement {",
        "    repositories {",
        "        gradlePluginPortal()",
        "        mavenCentral()",
        "    }",
        "}",
        "",
        "fun includeProject(pathName: String, dirName: String) {",
        "    include(pathName)",
        "    project(pathName).projectDir = file(dirName)",
        "}",
        "",
    ]
    for topic in TOPICS:
        for language in topic["languages"]:
            if language in {"java", "kotlin"}:
                lines.append(f'includeProject(":{gradle_path(topic, language)}", "topics/{topic["num"]:02d}-{topic["slug"]}/{language}")')
    return "\n".join(lines) + "\n"


def render_root_build_gradle() -> str:
    return text(
        """
        allprojects {
            group = "dev.reinvent.wheel"
            version = "0.1.0"
        }
        """
    )


def render_gradle_versions() -> str:
    return text(
        """
        [versions]
        junit = "5.13.1"
        kotlin = "2.3.10"
        coroutines = "1.10.2"
        h2 = "2.3.232"

        [libraries]
        junit-jupiter = { module = "org.junit.jupiter:junit-jupiter", version.ref = "junit" }
        junit-platform-launcher = { module = "org.junit.platform:junit-platform-launcher", version = "1.13.1" }
        kotlin-test-junit5 = { module = "org.jetbrains.kotlin:kotlin-test-junit5", version.ref = "kotlin" }
        kotlinx-coroutines-core = { module = "org.jetbrains.kotlinx:kotlinx-coroutines-core", version.ref = "coroutines" }
        h2 = { module = "com.h2database:h2", version.ref = "h2" }
        """
    )


def render_gradlew() -> str:
    return text(
        """
        #!/usr/bin/env bash
        set -euo pipefail
        REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
        source "$REPO_ROOT/scripts/env.sh"
        if [ -z "${GRADLE_BIN:-}" ] || [ ! -x "$GRADLE_BIN" ]; then
          echo "Gradle is not bootstrapped. Run make bootstrap first." >&2
          exit 1
        fi
        exec "$GRADLE_BIN" "$@"
        """
    )


def render_language_readme(topic: dict, language: str) -> str:
    lines = [f"# {topic['num']:02d}. {topic['title']} / {language}", "", "## 어디에 작성하나", ""]
    for label, path in topic_language_files(topic, language):
        relative_path = path.split("/", 1)[1] if path.startswith(f"{language}/") else path
        lines.append(f"- {label}: `{relative_path}`")
    lines.extend(
        [
            f"- 입력 fixture: `../fixtures/`",
            f"- e2e 스크립트: `../e2e/{language}-smoke.sh`",
            "",
            "## 템플릿 기본 상태",
            "",
            ("- 기본 서버 계약: `GET /health -> ok`, `POST /echo -> body 그대로`" if topic["kind"] == "http_server_router" else f"- 기본 출력: `{hello_output(topic).strip()}`"),
            "- CLI 스캐폴드: `main` 또는 `cli`가 `argv` 위치 계약만 이미 처리합니다.",
            "- 이 상태는 시작점일 뿐이며, 실제 미션 성공 기준은 `make e2e`와 `../SPEC.md`에 있습니다.",
            "- fresh scaffold 상태에서 `make e2e`는 실패해도 정상입니다.",
            "",
            "## 인자 위치 계약",
            "",
        ]
    )
    for contract in argv_contract(topic, scope="project"):
        lines.append(f"- {contract}")
    lines.extend(
        [
            "",
            "## 어떻게 작성하나",
            "",
            f"- {language_write_hint(language)}",
            "- 템플릿의 인자 개수, 위치, stdout 형식은 가능하면 유지하고 내부 구현만 교체하는 편이 가장 안전합니다.",
            "- `../SPEC.md`의 번호형 요구사항을 만족시키는 구현을 목표로 합니다.",
            "- `../QA.md`와 `../e2e/*.sh`가 실제 성공 기준입니다.",
            "- 빌드 산출물(`build/`, `target/`, `bin/`, `__pycache__/`)은 수정 대상이 아닙니다.",
            "",
            "## Make 명령",
            "",
        ]
    )
    for command in topic_language_commands(language, in_topic=False):
        lines.append(f"- {command}")
    lines.extend(["", "## make 없이 직접 실행하는 방법", ""])
    for command in direct_commands_for(topic, language):
        lines.append(f"- {command}")
    lines.extend(
        [
            "",
            "## 권장 구현 순서",
            "",
            "1. `../SPEC.md`에서 최종 미션 요구사항을 읽습니다.",
            "2. `../fixtures/expected.txt`로 hello baseline을 확인합니다." if topic["kind"] != "http_server_router" else "2. `make run` 또는 `make smoke`로 서버 baseline이 뜨는지 먼저 확인합니다.",
            "3. `../fixtures/mission-expected.txt` 또는 대응 fixture를 보고 e2e 성공 기준을 확인합니다." if topic["kind"] != "http_server_router" else "3. `../e2e/*.sh`를 열어서 health, echo, 오류 응답 기준을 확인합니다.",
            "4. 먼저 `make build`와 `make run`이 유지되도록 구현한 뒤, `make test`와 `make e2e`를 맞춥니다." if language != "python" else "4. 먼저 `make run`이 유지되도록 구현한 뒤, `make test`와 `make e2e`를 맞춥니다.",
        ]
    )
    return "\n".join(lines) + "\n"


def create_topic(topic: dict) -> None:
    base = topic_dir(topic)
    write(base / "README.md", render_topic_readme(topic))
    write(base / "SPEC.md", render_topic_spec(topic))
    write(base / "QA.md", render_topic_qa(topic))
    for name, content in fixtures_for(topic).items():
        target_dir = "sql" if name.endswith(".sql") else "fixtures"
        write(base / target_dir / name, content)
    for language in topic["languages"]:
        write(base / language / "README.md", render_language_readme(topic, language))
        if language == "rust":
            write(base / "e2e" / "rust-smoke.sh", render_rust_e2e(topic), executable=True)
            write(base / language / "Cargo.toml", render_rust_cargo_toml(topic))
            write(base / language / "Makefile", render_rust_makefile(topic))
            write(base / language / "src" / "lib.rs", rust_lib_code(topic))
            write(base / language / "src" / "main.rs", rust_main_code(topic))
            write(base / language / "tests" / "smoke.rs", render_rust_test(topic))
        elif language == "cpp":
            write(base / "e2e" / "cpp-smoke.sh", render_cpp_e2e(topic), executable=True)
            write(base / language / "Makefile", render_cpp_makefile(topic))
            write(base / language / "include" / "topic.hpp", render_cpp_header(topic))
            write(base / language / "src" / "lib.cpp", render_cpp_lib(topic))
            write(base / language / "src" / "main.cpp", render_cpp_main(topic))
            write(base / language / "tests" / "test_main.cpp", render_cpp_test(topic))
        elif language == "python":
            write(base / "e2e" / "python-smoke.sh", render_python_e2e(topic), executable=True)
            package = project_name(topic, "python")
            write(base / language / "pyproject.toml", render_python_pyproject(topic))
            write(base / language / "Makefile", render_python_makefile(topic))
            write(base / language / "src" / package / "__init__.py", "__all__ = []\n")
            write(base / language / "src" / package / "core.py", render_python_core(topic))
            write(base / language / "src" / package / "cli.py", render_python_cli(topic))
            write(base / language / "tests" / "test_topic.py", render_python_test(topic))
        elif language == "java":
            write(base / "e2e" / "java-smoke.sh", render_java_e2e(topic), executable=True)
            package_path = Path(*java_package(topic).split("."))
            write(base / language / "build.gradle.kts", render_java_build_gradle(topic))
            write(base / language / "Makefile", render_java_makefile(topic))
            write(base / language / "src" / "main" / "java" / package_path / f"{class_name(topic)}.java", render_java_source(topic))
            write(base / language / "src" / "test" / "java" / package_path / f"{class_name(topic)}Test.java", render_java_test(topic))
        elif language == "kotlin":
            write(base / "e2e" / "kotlin-smoke.sh", render_kotlin_e2e(topic), executable=True)
            package_path = Path(*java_package(topic).split("."))
            write(base / language / "build.gradle.kts", render_kotlin_build_gradle(topic))
            write(base / language / "Makefile", render_kotlin_makefile(topic))
            write(base / language / "src" / "main" / "kotlin" / package_path / f"{class_name(topic)}.kt", render_kotlin_source(topic))
            write(base / language / "src" / "test" / "kotlin" / package_path / f"{class_name(topic)}Test.kt", render_kotlin_test(topic))
    if topic["kind"] in {"batch_etl_pipeline", "parallel_log_analyzer", "mini_mapreduce"}:
        write(base / "shell" / "README.md", text(f"# {topic['num']:02d}. {topic['title']} / shell\n\n보조 파이프라인 스크립트 자리.\n"))


def main() -> None:
    write(ROOT / "HAND_CODING_TOPICS.md", render_hand_coding_topics())
    write(ROOT / "README.md", render_root_readme())
    write(ROOT / ".gitignore", render_gitignore())
    write(ROOT / "Makefile", render_root_makefile())
    write(ROOT / "Cargo.toml", render_cargo_toml())
    write(ROOT / "settings.gradle.kts", render_settings_gradle())
    write(ROOT / "build.gradle.kts", render_root_build_gradle())
    write(ROOT / "gradle.properties", text("org.gradle.jvmargs=-Xmx2g -Dfile.encoding=UTF-8\norg.gradle.daemon=false\n"))
    write(ROOT / "gradle" / "libs.versions.toml", render_gradle_versions())
    write(ROOT / "gradle" / "wrapper" / "gradle-wrapper.properties", text("distributionBase=GRADLE_USER_HOME\ndistributionPath=wrapper/dists\ndistributionUrl=https\\://services.gradle.org/distributions/gradle-9.4.0-bin.zip\nzipStoreBase=GRADLE_USER_HOME\nzipStorePath=wrapper/dists\n"))
    write(ROOT / "gradlew", render_gradlew(), executable=True)
    write(ROOT / "toolchains" / "versions.env", render_versions_env())
    write(ROOT / "scripts" / "env.sh", render_env_sh(), executable=True)
    write(ROOT / "scripts" / "bootstrap-rust.sh", render_bootstrap_rust(), executable=True)
    write(ROOT / "scripts" / "bootstrap-jdk.sh", render_bootstrap_jdk(), executable=True)
    write(ROOT / "scripts" / "bootstrap-gradle.sh", render_bootstrap_gradle(), executable=True)
    write(ROOT / "scripts" / "bootstrap-python.sh", render_bootstrap_python(), executable=True)
    write(ROOT / "scripts" / "list-projects.py", render_list_projects(), executable=True)
    write(ROOT / "scripts" / "verify-all.sh", render_verify_all(), executable=True)
    write(ROOT / "scripts" / "smoke-all.sh", render_smoke_all(), executable=True)
    write(ROOT / "artifacts" / ".gitkeep", "")
    for topic in TOPICS:
        create_topic(topic)


if __name__ == "__main__":
    main()
