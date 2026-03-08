from __future__ import annotations

import json

from scaffold_catalog import cli_options, hello_output, project_name, run_args_for, text


def render_python_pyproject(topic: dict) -> str:
    dependencies = []
    if topic["kind"] in {"mini_groupby_engine", "windowed_timeseries_analyzer"}:
        dependencies.append('"duckdb>=1.3.2"')
    dep_block = ""
    if dependencies:
        dep_block = "dependencies = [\n" + "\n".join(f"    {line}" for line in dependencies) + "\n]\n"
    return text(
        f"""
        [project]
        name = "{project_name(topic, 'python')}"
        version = "0.1.0"
        requires-python = ">=3.14"
        {dep_block}[build-system]
        requires = ["setuptools>=68"]
        build-backend = "setuptools.build_meta"
        """
    )


def render_python_makefile(topic: dict) -> str:
    package = project_name(topic, "python")
    return text(
        f"""
        SHELL := /bin/bash
        REPO_ROOT := $(abspath ../../..)
        .PHONY: run test e2e smoke

        run:
        \tbash -lc 'source "$(REPO_ROOT)/scripts/env.sh" && export PYTHONPATH="$(CURDIR)/src" && "$$PYTHON_BIN" -m {package}.cli {run_args_for(topic, "python")}'

        test:
        \tbash -lc 'source "$(REPO_ROOT)/scripts/env.sh" && export PYTHONPATH="$(CURDIR)/src" && "$$PYTHON_BIN" -m unittest discover -s tests'

        e2e:
        \tbash ../e2e/python-smoke.sh

        smoke:
        \t$(MAKE) run
        """
    )


def render_python_e2e(topic: dict) -> str:
    return text(
        f"""
        #!/usr/bin/env bash
        set -euo pipefail
        ROOT="$(cd "$(dirname "${{BASH_SOURCE[0]}}")/.." && pwd)"
        TOPIC_NAME="${{ROOT##*/}}"
        SCRIPT_NAME="${{BASH_SOURCE[0]##*/}}"
        LANGUAGE="${{SCRIPT_NAME%-smoke.sh}}"
        pushd "$ROOT/python" >/dev/null
        make -s --no-print-directory run > /tmp/{topic['slug']}-python-out.txt
        if ! diff -u "$ROOT/fixtures/mission-expected.txt" /tmp/{topic['slug']}-python-out.txt; then
          echo "Mission not complete for Python: implement the topic until stdout matches fixtures/mission-expected.txt" >&2
          exit 1
        fi
        echo "E2E PASS: $TOPIC_NAME ($LANGUAGE)"
        popd >/dev/null
        """
    )


def render_python_core(topic: dict) -> str:
    lines = [
        "from dataclasses import dataclass",
        "",
        "",
        "@dataclass(frozen=True)",
        "class CliArgs:",
    ]
    for option in cli_options(topic):
        if option["type"] == "int":
            lines.append(f"    {option['name']}: int = {option['default']}")
        else:
            lines.append(f"    {option['name']}: str")
    lines.extend(
        [
            "",
            "",
            "def run(args: CliArgs) -> str:",
            "    _ = args",
            f"    return {json.dumps(hello_output(topic))}",
        ]
    )
    return "\n".join(lines) + "\n"


def python_usage(topic: dict) -> str:
    parts = []
    for option in cli_options(topic):
        label = f"<{option['name']}>" if option.get("required", True) else f"[{option['name']}]"
        parts.append(label)
    suffix = f" {' '.join(parts)}" if parts else ""
    return f"usage: python -m {project_name(topic, 'python')}.cli{suffix}"


def render_python_cli(topic: dict) -> str:
    options = cli_options(topic)
    required_count = sum(1 for option in options if option.get("required", True))
    lines = [
        "import sys",
        "",
        "from .core import CliArgs, run",
        "",
        "",
        "def parse_args(argv: list[str] | None = None) -> CliArgs:",
        "    values = sys.argv[1:] if argv is None else argv",
    ]
    if required_count == 0:
        lines.extend(
            [
            f"    if len(values) > {len(options)}:",
            f'        raise SystemExit("{python_usage(topic)}")',
            ]
        )
    else:
        lines.extend(
            [
            f"    if len(values) < {required_count} or len(values) > {len(options)}:",
            f'        raise SystemExit("{python_usage(topic)}")',
            ]
        )
    lines.append("    return CliArgs(")
    for index, option in enumerate(options):
        if option["type"] == "int":
            if option.get("required", True):
                lines.append(f"        {option['name']}=int(values[{index}]),")
            else:
                lines.append(
                    f"        {option['name']}=int(values[{index}]) if len(values) > {index} else {option['default']},"
                )
        else:
            lines.append(f"        {option['name']}=values[{index}],")
    lines.extend(
        [
            "    )",
            "",
            "",
            "def main() -> None:",
            "    print(run(parse_args()), end=\"\")",
            "",
            "",
            "if __name__ == \"__main__\":",
            "    main()",
        ]
    )
    return "\n".join(lines) + "\n"


def render_python_test(topic: dict) -> str:
    package = project_name(topic, "python")
    lines = [
        "import unittest",
        "",
        f"from {package}.core import CliArgs, run",
        "",
        "",
        "class TopicTests(unittest.TestCase):",
        "    def test_minimal_template_message(self) -> None:",
        "        args = CliArgs(",
    ]
    for option in cli_options(topic):
        if option["type"] == "int":
            lines.append(f"            {option['name']}={option['default']},")
        else:
            lines.append(f"            {option['name']}={json.dumps(str(option['value']))},")
    lines.extend(
        [
            "        )",
            f"        self.assertEqual(run(args), {json.dumps(hello_output(topic))})",
            "",
            "",
            "if __name__ == \"__main__\":",
            "    unittest.main()",
        ]
    )
    return "\n".join(lines) + "\n"
