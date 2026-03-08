from __future__ import annotations

import json

from scaffold_catalog import cli_options, hello_output, project_name, run_args_for, text


def cpp_type(option: dict[str, object]) -> str:
    return "int" if option["type"] == "int" else "std::string"


def render_cpp_makefile(topic: dict) -> str:
    app = project_name(topic, "cpp")
    return text(
        f"""
        CXX ?= g++
        CXXFLAGS ?= -std=c++23 -O2 -Wall -Wextra -pedantic -Iinclude
        BIN_DIR := bin
        APP := $(BIN_DIR)/{app}
        TEST_BIN := $(BIN_DIR)/{app}_tests
        .PHONY: build run test e2e smoke clean

        $(APP): src/main.cpp src/lib.cpp include/topic.hpp
        \tmkdir -p $(BIN_DIR)
        \t$(CXX) $(CXXFLAGS) src/main.cpp src/lib.cpp -o $(APP)

        $(TEST_BIN): tests/test_main.cpp src/lib.cpp include/topic.hpp
        \tmkdir -p $(BIN_DIR)
        \t$(CXX) $(CXXFLAGS) tests/test_main.cpp src/lib.cpp -o $(TEST_BIN)

        build: $(APP) $(TEST_BIN)

        run: $(APP)
        \t./$(APP) {run_args_for(topic, "cpp")}

        test: $(TEST_BIN)
        \t./$(TEST_BIN)

        e2e:
        \tbash ../e2e/cpp-smoke.sh

        smoke: run

        clean:
        \trm -rf $(BIN_DIR)
        """
    )


def render_cpp_e2e(topic: dict) -> str:
    return text(
        f"""
        #!/usr/bin/env bash
        set -euo pipefail
        ROOT="$(cd "$(dirname "${{BASH_SOURCE[0]}}")/.." && pwd)"
        pushd "$ROOT/cpp" >/dev/null
        make -s --no-print-directory run > /tmp/{topic['slug']}-cpp-out.txt
        if ! diff -u "$ROOT/fixtures/mission-expected.txt" /tmp/{topic['slug']}-cpp-out.txt; then
          echo "Mission not complete for C++: implement the topic until stdout matches fixtures/mission-expected.txt" >&2
          exit 1
        fi
        popd >/dev/null
        """
    )


def render_cpp_header(topic: dict) -> str:
    lines = [
        "#pragma once",
        "#include <string>",
        "",
        "struct CliArgs {",
    ]
    for option in cli_options(topic):
        default = ""
        if option["type"] == "int":
            default = f"{{{option['default']}}}"
        lines.append(f"  {cpp_type(option)} {option['name']}{default};")
    lines.extend(["};", "", "std::string run(const CliArgs& args);"])
    return "\n".join(lines) + "\n"


def render_cpp_lib(topic: dict) -> str:
    return text(
        f"""
        #include "topic.hpp"

        std::string run(const CliArgs& args) {{
          (void)args;
          return {json.dumps(hello_output(topic))};
        }}
        """
    )


def cpp_usage(topic: dict) -> str:
    parts = []
    for option in cli_options(topic):
        label = f"<{option['name']}>" if option.get("required", True) else f"[{option['name']}]"
        parts.append(label)
    suffix = f" {' '.join(parts)}" if parts else ""
    return f"usage: {project_name(topic, 'cpp')}{suffix}"


def render_cpp_main(topic: dict) -> str:
    options = cli_options(topic)
    required_count = sum(1 for option in options if option.get("required", True))
    lines = [
        '#include "topic.hpp"',
        "#include <iostream>",
        "#include <stdexcept>",
        "#include <string>",
        "",
        "namespace {",
        "CliArgs parse_args(int argc, char** argv) {",
    ]
    if required_count == 0:
        lines.extend(
            [
                f"  if (argc - 1 > {len(options)}) {{",
                f'    throw std::runtime_error("{cpp_usage(topic)}");',
                "  }",
            ]
        )
    else:
        lines.extend(
            [
                f"  if (argc - 1 < {required_count} || argc - 1 > {len(options)}) {{",
                f'    throw std::runtime_error("{cpp_usage(topic)}");',
                "  }",
            ]
        )
    lines.extend(
        [
        "  CliArgs parsed{};",
        ]
    )
    for index, option in enumerate(options, start=1):
        arg_ref = f"argv[{index}]"
        if option["type"] == "int":
            if option.get("required", True):
                lines.append(f"  parsed.{option['name']} = std::stoi({arg_ref});")
            else:
                lines.append(f"  if (argc > {index}) parsed.{option['name']} = std::stoi({arg_ref});")
        else:
            lines.append(f"  parsed.{option['name']} = {arg_ref};")
    lines.extend(
        [
            "  return parsed;",
            "}",
            "}",
            "",
            "int main(int argc, char** argv) {",
            "  try {",
            "    auto args = parse_args(argc, argv);",
            "    std::cout << run(args);",
            "    return 0;",
            "  } catch (const std::exception& ex) {",
            '    std::cerr << ex.what() << "\\n";',
            "    return 1;",
            "  }",
            "}",
        ]
    )
    return "\n".join(lines) + "\n"


def render_cpp_test(topic: dict) -> str:
    args = ["  CliArgs args{};"]
    for option in cli_options(topic):
        if option["type"] == "int":
            args.append(f"  args.{option['name']} = {option['default']};")
        else:
            args.append(f"  args.{option['name']} = {json.dumps(str(option['value']))};")
    return text(
        f"""
        #include "topic.hpp"
        #include <cassert>

        int main() {{
        {'\n'.join(args)}
          assert(run(args) == {json.dumps(hello_output(topic))});
          return 0;
        }}
        """
    )
