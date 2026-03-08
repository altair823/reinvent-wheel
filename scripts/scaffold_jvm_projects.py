from __future__ import annotations

import json
import textwrap

from scaffold_catalog import class_name, cli_options, gradle_path, hello_output, java_package, run_args_for, text


def indented_lines(block: str, prefix: str = "    ") -> list[str]:
    stripped = block.strip()
    if not stripped:
        return []
    return textwrap.indent(stripped, prefix).splitlines()


def render_java_makefile(topic: dict) -> str:
    project_path = f":{gradle_path(topic, 'java')}"
    run_args = run_args_for(topic, "java")
    run_task = f"./gradlew -q $(PROJECT_PATH):run --args='{run_args}'" if run_args else "./gradlew -q $(PROJECT_PATH):run"
    smoke = "\tbash ../e2e/java-smoke.sh baseline" if topic["kind"] == "http_server_router" else "\t$(MAKE) run"
    return "\n".join(
        [
            "SHELL := /bin/bash",
            "REPO_ROOT := $(abspath ../../..)",
            f"PROJECT_PATH := {project_path}",
            ".PHONY: build run test e2e smoke",
            "",
            "build:",
            '\tbash -lc "cd \'$(REPO_ROOT)\' && ./gradlew $(PROJECT_PATH):installDist"',
            "",
            "run:",
            f'\tbash -lc "cd \'$(REPO_ROOT)\' && {run_task}"',
            "",
            "test:",
            '\tbash -lc "cd \'$(REPO_ROOT)\' && ./gradlew $(PROJECT_PATH):test"',
            "",
            "e2e:",
            "\tbash ../e2e/java-smoke.sh",
            "",
            "smoke:",
            smoke,
            "",
        ]
    )


def render_kotlin_makefile(topic: dict) -> str:
    project_path = f":{gradle_path(topic, 'kotlin')}"
    run_args = run_args_for(topic, "kotlin")
    run_task = f"./gradlew -q $(PROJECT_PATH):run --args='{run_args}'" if run_args else "./gradlew -q $(PROJECT_PATH):run"
    smoke = "\tbash ../e2e/kotlin-smoke.sh baseline" if topic["kind"] == "http_server_router" else "\t$(MAKE) run"
    return "\n".join(
        [
            "SHELL := /bin/bash",
            "REPO_ROOT := $(abspath ../../..)",
            f"PROJECT_PATH := {project_path}",
            ".PHONY: build run test e2e smoke",
            "",
            "build:",
            '\tbash -lc "cd \'$(REPO_ROOT)\' && ./gradlew $(PROJECT_PATH):installDist"',
            "",
            "run:",
            f'\tbash -lc "cd \'$(REPO_ROOT)\' && {run_task}"',
            "",
            "test:",
            '\tbash -lc "cd \'$(REPO_ROOT)\' && ./gradlew $(PROJECT_PATH):test"',
            "",
            "e2e:",
            "\tbash ../e2e/kotlin-smoke.sh",
            "",
            "smoke:",
            smoke,
            "",
        ]
    )


def render_java_build_gradle(topic: dict) -> str:
    extra = "    implementation(libs.h2)\n" if topic["kind"] == "jdbc_todo_cli" else ""
    return text(
        f"""
        plugins {{
            application
            java
        }}

        java {{
            toolchain {{
                languageVersion.set(JavaLanguageVersion.of(25))
            }}
        }}

        dependencies {{
            testImplementation(libs.junit.jupiter)
            testRuntimeOnly(libs.junit.platform.launcher)
        {extra}}}

        tasks.test {{
            useJUnitPlatform()
        }}

        application {{
            mainClass.set("{java_package(topic)}.{class_name(topic)}")
        }}
        """
    )


def render_kotlin_build_gradle(topic: dict) -> str:
    extra = "    implementation(libs.kotlinx.coroutines.core)\n" if topic["kind"] == "coroutine_scheduler" else ""
    return text(
        f"""
        plugins {{
            application
            kotlin("jvm") version "2.3.10"
        }}

        kotlin {{
            jvmToolchain(25)
        }}

        dependencies {{
            testImplementation(libs.kotlin.test.junit5)
            testRuntimeOnly(libs.junit.platform.launcher)
        {extra}}}

        tasks.test {{
            useJUnitPlatform()
        }}

        application {{
            mainClass.set("{java_package(topic)}.{class_name(topic)}Kt")
        }}
        """
    )


def render_java_e2e(topic: dict) -> str:
    if topic["kind"] == "http_server_router":
        return text(
            f"""
            #!/usr/bin/env bash
            set -euo pipefail
            MODE="${{1:-mission}}"
            ROOT="$(cd "$(dirname "${{BASH_SOURCE[0]}}")/.." && pwd)"
            TOPIC_NAME="${{ROOT##*/}}"
            SCRIPT_NAME="${{BASH_SOURCE[0]##*/}}"
            LANGUAGE="${{SCRIPT_NAME%-smoke.sh}}"
            PORT="${{PORT:-18081}}"
            export PORT
            pushd "$ROOT/java" >/dev/null
            make -s --no-print-directory run > /tmp/{topic['slug']}-java.log 2>&1 &
            pid=$!
            trap 'kill $pid 2>/dev/null || true; wait $pid 2>/dev/null || true' EXIT
            for _ in $(seq 1 160); do
              if curl -fsS "http://127.0.0.1:$PORT/health" > /tmp/{topic['slug']}-java-health.txt 2>/dev/null; then
                break
              fi
              sleep 0.25
            done
            curl -fsS -X POST --data-binary @"$ROOT/fixtures/echo-body.txt" "http://127.0.0.1:$PORT/echo" > /tmp/{topic['slug']}-java-echo.txt
            diff -u "$ROOT/fixtures/expected-health.txt" /tmp/{topic['slug']}-java-health.txt
            diff -u "$ROOT/fixtures/expected-echo.txt" /tmp/{topic['slug']}-java-echo.txt
            if [ "$MODE" = "mission" ]; then
              status_404="$(curl -s -o /tmp/{topic['slug']}-java-404.txt -w '%{{http_code}}' "http://127.0.0.1:$PORT/missing")"
              if [ "$status_404" != "404" ]; then
                echo "Mission not complete: expected 404 for unknown route, got $status_404" >&2
                exit 1
              fi
              status_405="$(curl -s -o /tmp/{topic['slug']}-java-405.txt -w '%{{http_code}}' "http://127.0.0.1:$PORT/echo")"
              if [ "$status_405" != "405" ]; then
                echo "Mission not complete: expected 405 for GET /echo, got $status_405" >&2
                exit 1
              fi
            fi
            echo "E2E PASS: $TOPIC_NAME ($LANGUAGE, mode=$MODE)"
            popd >/dev/null
            """
        )
    return text(
        f"""
        #!/usr/bin/env bash
        set -euo pipefail
        ROOT="$(cd "$(dirname "${{BASH_SOURCE[0]}}")/.." && pwd)"
        TOPIC_NAME="${{ROOT##*/}}"
        SCRIPT_NAME="${{BASH_SOURCE[0]##*/}}"
        LANGUAGE="${{SCRIPT_NAME%-smoke.sh}}"
        pushd "$ROOT/java" >/dev/null
        make -s --no-print-directory run > /tmp/{topic['slug']}-java-out.txt
        if ! diff -u "$ROOT/fixtures/mission-expected.txt" /tmp/{topic['slug']}-java-out.txt; then
          echo "Mission not complete for Java: implement the topic until stdout matches fixtures/mission-expected.txt" >&2
          exit 1
        fi
        echo "E2E PASS: $TOPIC_NAME ($LANGUAGE)"
        popd >/dev/null
        """
    )


def render_kotlin_e2e(topic: dict) -> str:
    if topic["kind"] == "http_server_router":
        return text(
            f"""
            #!/usr/bin/env bash
            set -euo pipefail
            MODE="${{1:-mission}}"
            ROOT="$(cd "$(dirname "${{BASH_SOURCE[0]}}")/.." && pwd)"
            TOPIC_NAME="${{ROOT##*/}}"
            SCRIPT_NAME="${{BASH_SOURCE[0]##*/}}"
            LANGUAGE="${{SCRIPT_NAME%-smoke.sh}}"
            PORT="${{PORT:-18082}}"
            export PORT
            pushd "$ROOT/kotlin" >/dev/null
            make -s --no-print-directory run > /tmp/{topic['slug']}-kotlin.log 2>&1 &
            pid=$!
            trap 'kill $pid 2>/dev/null || true; wait $pid 2>/dev/null || true' EXIT
            for _ in $(seq 1 160); do
              if curl -fsS "http://127.0.0.1:$PORT/health" > /tmp/{topic['slug']}-kotlin-health.txt 2>/dev/null; then
                break
              fi
              sleep 0.25
            done
            curl -fsS -X POST --data-binary @"$ROOT/fixtures/echo-body.txt" "http://127.0.0.1:$PORT/echo" > /tmp/{topic['slug']}-kotlin-echo.txt
            diff -u "$ROOT/fixtures/expected-health.txt" /tmp/{topic['slug']}-kotlin-health.txt
            diff -u "$ROOT/fixtures/expected-echo.txt" /tmp/{topic['slug']}-kotlin-echo.txt
            if [ "$MODE" = "mission" ]; then
              status_404="$(curl -s -o /tmp/{topic['slug']}-kotlin-404.txt -w '%{{http_code}}' "http://127.0.0.1:$PORT/missing")"
              if [ "$status_404" != "404" ]; then
                echo "Mission not complete: expected 404 for unknown route, got $status_404" >&2
                exit 1
              fi
              status_405="$(curl -s -o /tmp/{topic['slug']}-kotlin-405.txt -w '%{{http_code}}' "http://127.0.0.1:$PORT/echo")"
              if [ "$status_405" != "405" ]; then
                echo "Mission not complete: expected 405 for GET /echo, got $status_405" >&2
                exit 1
              fi
            fi
            echo "E2E PASS: $TOPIC_NAME ($LANGUAGE, mode=$MODE)"
            popd >/dev/null
            """
        )
    return text(
        f"""
        #!/usr/bin/env bash
        set -euo pipefail
        ROOT="$(cd "$(dirname "${{BASH_SOURCE[0]}}")/.." && pwd)"
        TOPIC_NAME="${{ROOT##*/}}"
        SCRIPT_NAME="${{BASH_SOURCE[0]##*/}}"
        LANGUAGE="${{SCRIPT_NAME%-smoke.sh}}"
        pushd "$ROOT/kotlin" >/dev/null
        make -s --no-print-directory run > /tmp/{topic['slug']}-kotlin-out.txt
        if ! diff -u "$ROOT/fixtures/mission-expected.txt" /tmp/{topic['slug']}-kotlin-out.txt; then
          echo "Mission not complete for Kotlin: implement the topic until stdout matches fixtures/mission-expected.txt" >&2
          exit 1
        fi
        echo "E2E PASS: $TOPIC_NAME ($LANGUAGE)"
        popd >/dev/null
        """
    )


def java_record_components(topic: dict) -> str:
    options = cli_options(topic)
    if not options:
        return ""
    return ", ".join(f"{'int' if option['type'] == 'int' else 'String'} {option['name']}" for option in options)


def java_usage(topic: dict, language: str) -> str:
    parts = []
    for option in cli_options(topic):
        label = f"<{option['name']}>" if option.get("required", True) else f"[{option['name']}]"
        parts.append(label)
    suffix = f" {' '.join(parts)}" if parts else ""
    return f"usage: {gradle_path(topic, language)}{suffix}"


def java_parse_args_method(topic: dict) -> str:
    options = cli_options(topic)
    if not options:
        return "\n".join(
            [
                "public static CliArgs parseArgs(String[] args) {",
                "    if (args.length != 0) {",
                '        throw new IllegalArgumentException("this template does not accept command-line arguments");',
                "    }",
                "    return new CliArgs();",
                "}",
            ]
        )
    lines = ["public static CliArgs parseArgs(String[] args) {"]
    required_count = sum(1 for option in options if option.get("required", True))
    if required_count == 0:
        lines.extend(
            [
                f"    if (args.length > {len(options)}) {{",
                f'        throw new IllegalArgumentException("{java_usage(topic, "java")}");',
                "    }",
            ]
        )
    else:
        lines.extend(
            [
                f"    if (args.length < {required_count} || args.length > {len(options)}) {{",
                f'        throw new IllegalArgumentException("{java_usage(topic, "java")}");',
                "    }",
            ]
        )
    for index, option in enumerate(options):
        name = option["name"]
        if name == "port":
            lines.append(
                '    int port = args.length > 0 ? parseInt(args[0], "argv[1]") : Integer.parseInt(System.getenv().getOrDefault("PORT", "18080"));'
            )
        elif option["type"] == "int":
            if option.get("required", True):
                lines.append(f'    int {name} = parseInt(args[{index}], "argv[{index + 1}]");')
            else:
                lines.append(
                    f'    int {name} = args.length > {index} ? parseInt(args[{index}], "argv[{index + 1}]") : {option["default"]};'
                )
        else:
            lines.append(f"    String {name} = args[{index}];")
    ctor_args = ", ".join(str(option["name"]) for option in options)
    lines.append(f"    return new CliArgs({ctor_args});")
    lines.append("}")
    return "\n".join(lines)


def java_helpers_method(topic: dict) -> str:
    if not any(option["type"] == "int" for option in cli_options(topic)):
        return ""
    return text(
        """
        private static int parseInt(String value, String label) {
            try {
                return Integer.parseInt(value);
            } catch (NumberFormatException ex) {
                throw new IllegalArgumentException(label + " must be an integer: " + value, ex);
            }
        }
        """
    )


def render_java_source(topic: dict) -> str:
    pkg = java_package(topic)
    name = class_name(topic)
    components = java_record_components(topic)
    parse_args = java_parse_args_method(topic)
    helpers = java_helpers_method(topic)
    lines = [f"package {pkg};", ""]
    if topic["kind"] == "http_server_router":
        lines.extend(
            [
                "import com.sun.net.httpserver.HttpExchange;",
                "import com.sun.net.httpserver.HttpServer;",
                "import java.io.IOException;",
                "import java.net.InetSocketAddress;",
                "import java.nio.charset.StandardCharsets;",
                "",
            ]
        )
    lines.extend(
        [
            f"public final class {name} {{",
            f"    public record CliArgs({components}) {{",
            "    }",
            "",
            f"    private {name}() {{",
            "    }",
        ]
    )
    if helpers:
        lines.append("")
        lines.extend(indented_lines(helpers))
    lines.append("")
    lines.extend(indented_lines(parse_args))
    if topic["kind"] == "http_server_router":
        server_block = text(
            """
            static HttpServer start(int port) throws IOException {
                var server = HttpServer.create(new InetSocketAddress("127.0.0.1", port), 0);
                server.createContext("/health", exchange -> {
                    if (!"GET".equals(exchange.getRequestMethod())) {
                        send(exchange, 405, "method-not-allowed\\n");
                        return;
                    }
                    send(exchange, 200, "ok\\n");
                });
                server.createContext("/echo", exchange -> {
                    if (!"POST".equals(exchange.getRequestMethod())) {
                        send(exchange, 405, "method-not-allowed\\n");
                        return;
                    }
                    send(exchange, 200, new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8));
                });
                server.createContext("/", exchange -> send(exchange, 404, "not-found\\n"));
                server.start();
                return server;
            }

            private static void send(HttpExchange exchange, int status, String body) throws IOException {
                byte[] bytes = body.getBytes(StandardCharsets.UTF_8);
                exchange.sendResponseHeaders(status, bytes.length);
                exchange.getResponseBody().write(bytes);
                exchange.close();
            }

            public static void main(String[] args) throws Exception {
                CliArgs cliArgs = parseArgs(args);
                start(cliArgs.port());
                Thread.currentThread().join();
            }
            """
        )
        lines.append("")
        lines.extend(indented_lines(server_block))
    else:
        simple_block = text(
            f"""
            public static String helloMessage(CliArgs args) {{
                var ignored = args;
                return {json.dumps(hello_output(topic))};
            }}

            public static void main(String[] args) {{
                System.out.print(helloMessage(parseArgs(args)));
            }}
            """
        )
        lines.append("")
        lines.extend(indented_lines(simple_block))
    lines.append("}")
    return "\n".join(lines) + "\n"


def render_java_test(topic: dict) -> str:
    pkg = java_package(topic)
    name = class_name(topic)
    if topic["kind"] == "http_server_router":
        body = f"{name}.CliArgs args = new {name}.CliArgs(18081);\n        assertDoesNotThrow(() -> {name}.start(args.port()).stop(0));"
    else:
        ctor = ", ".join(
            str(option["default"]) if option["type"] == "int" else json.dumps(str(option["value"]))
            for option in cli_options(topic)
        )
        body = f'assertEquals({json.dumps(hello_output(topic))}, {name}.helloMessage(new {name}.CliArgs({ctor})));'
    return text(
        f"""
        package {pkg};

        import static org.junit.jupiter.api.Assertions.*;

        import org.junit.jupiter.api.Test;

        final class {name}Test {{
            @Test
            void minimalTemplateCompilesAndRuns() {{
                {body}
            }}
        }}
        """
    )


def kotlin_constructor_params(topic: dict) -> str:
    options = cli_options(topic)
    if not options:
        return ""
    return ", ".join(f"val {option['name']}: {'Int' if option['type'] == 'int' else 'String'}" for option in options)


def kotlin_usage(topic: dict) -> str:
    parts = []
    for option in cli_options(topic):
        label = f"<{option['name']}>" if option.get("required", True) else f"[{option['name']}]"
        parts.append(label)
    suffix = f" {' '.join(parts)}" if parts else ""
    return f"usage: {gradle_path(topic, 'kotlin')}{suffix}"


def kotlin_parse_args(topic: dict) -> str:
    options = cli_options(topic)
    if not options:
        return "\n".join(
            [
                "fun parseArgs(args: Array<String>): CliArgs {",
                "    if (args.isNotEmpty()) {",
                '        throw IllegalArgumentException("this template does not accept command-line arguments")',
                "    }",
                "    return CliArgs()",
                "}",
            ]
        )
    lines = ["fun parseArgs(args: Array<String>): CliArgs {"]
    required_count = sum(1 for option in options if option.get("required", True))
    if required_count == 0:
        lines.extend(
            [
                f"    if (args.size > {len(options)}) {{",
                f'        throw IllegalArgumentException("{kotlin_usage(topic)}")',
                "    }",
            ]
        )
    else:
        lines.extend(
            [
                f"    if (args.size < {required_count} || args.size > {len(options)}) {{",
                f'        throw IllegalArgumentException("{kotlin_usage(topic)}")',
                "    }",
            ]
        )
    for index, option in enumerate(options):
        name = option["name"]
        if name == "port":
            lines.append(
                '    val port = if (args.isNotEmpty()) parseInt(args[0], "argv[1]") else System.getenv("PORT")?.let { parseInt(it, "PORT") } ?: 18080'
            )
        elif option["type"] == "int":
            if option.get("required", True):
                lines.append(f'    val {name} = parseInt(args[{index}], "argv[{index + 1}]")')
            else:
                lines.append(
                    f'    val {name} = if (args.size > {index}) parseInt(args[{index}], "argv[{index + 1}]") else {option["default"]}'
                )
        else:
            lines.append(f"    val {name} = args[{index}]")
    ctor_args = ", ".join(str(option["name"]) for option in options)
    lines.append(f"    return CliArgs({ctor_args})")
    lines.append("}")
    return "\n".join(lines)


def kotlin_helpers(topic: dict) -> str:
    if not any(option["type"] == "int" for option in cli_options(topic)):
        return ""
    return text(
        """
        private fun parseInt(value: String, label: String): Int {
            return value.toIntOrNull() ?: throw IllegalArgumentException("$label must be an integer: $value")
        }
        """
    )


def render_kotlin_source(topic: dict) -> str:
    pkg = java_package(topic)
    name = class_name(topic)
    params = kotlin_constructor_params(topic)
    helpers = kotlin_helpers(topic)
    parse_args = kotlin_parse_args(topic)
    lines = [f"package {pkg}", ""]
    if topic["kind"] == "http_server_router":
        lines.extend(
            [
                "import com.sun.net.httpserver.HttpExchange",
                "import com.sun.net.httpserver.HttpServer",
                "import java.net.InetSocketAddress",
                "",
            ]
        )
    lines.extend(
        [
            f"object {name} {{",
            f"    data class CliArgs({params})",
        ]
    )
    if helpers:
        lines.append("")
        lines.extend(indented_lines(helpers))
    lines.append("")
    lines.extend(indented_lines(parse_args))
    if topic["kind"] == "http_server_router":
        server_block = text(
            """
            fun start(port: Int): HttpServer {
                val server = HttpServer.create(InetSocketAddress("127.0.0.1", port), 0)
                server.createContext("/health") { exchange ->
                    if (exchange.requestMethod != "GET") {
                        send(exchange, 405, "method-not-allowed\\n")
                    } else {
                        send(exchange, 200, "ok\\n")
                    }
                }
                server.createContext("/echo") { exchange ->
                    if (exchange.requestMethod != "POST") {
                        send(exchange, 405, "method-not-allowed\\n")
                    } else {
                        send(exchange, 200, exchange.requestBody.readBytes().decodeToString())
                    }
                }
                server.createContext("/") { exchange ->
                    send(exchange, 404, "not-found\\n")
                }
                server.start()
                return server
            }

            private fun send(exchange: HttpExchange, status: Int, body: String) {
                val bytes = body.toByteArray()
                exchange.sendResponseHeaders(status, bytes.size.toLong())
                exchange.responseBody.use { it.write(bytes) }
                exchange.close()
            }
            """
        )
        lines.append("")
        lines.extend(indented_lines(server_block))
        lines.append("}")
        lines.append("")
        lines.extend(
            [
                "fun main(args: Array<String>) {",
                f"    val cliArgs = {name}.parseArgs(args)",
                f"    {name}.start(cliArgs.port)",
                "    Thread.currentThread().join()",
                "}",
            ]
        )
    else:
        simple_block = text(
            f"""
            fun helloMessage(args: CliArgs): String {{
                val ignored = args
                return {json.dumps(hello_output(topic))}
            }}
            """
        )
        lines.append("")
        lines.extend(indented_lines(simple_block))
        lines.append("}")
        lines.append("")
        lines.extend(
            [
                "fun main(args: Array<String>) {",
                f"    print({name}.helloMessage({name}.parseArgs(args)))",
                "}",
            ]
        )
    return "\n".join(lines) + "\n"


def render_kotlin_test(topic: dict) -> str:
    pkg = java_package(topic)
    name = class_name(topic)
    if topic["kind"] == "http_server_router":
        body = f"val args = {name}.CliArgs(18082)\n        {name}.start(args.port).stop(0)\n        kotlin.test.assertTrue(true)"
    else:
        ctor = ", ".join(
            str(option["default"]) if option["type"] == "int" else json.dumps(str(option["value"]))
            for option in cli_options(topic)
        )
        body = f'kotlin.test.assertEquals({json.dumps(hello_output(topic))}, {name}.helloMessage({name}.CliArgs({ctor})))'
    return text(
        f"""
        package {pkg}

        import kotlin.test.Test

        class {name}Test {{
            @Test
            fun minimalTemplateCompilesAndRuns() {{
                {body}
            }}
        }}
        """
    )
