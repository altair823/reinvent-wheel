from __future__ import annotations

import json

from scaffold_catalog import cli_options, hello_output, project_name, run_args_for, text


def rust_scalar_type(option: dict[str, object]) -> str:
    if option["name"] == "port":
        return "u16"
    if option["type"] == "int":
        return "usize"
    return "String"


def render_rust_makefile(topic: dict) -> str:
    run_args = run_args_for(topic, "rust")
    lines = [
        "SHELL := /bin/bash",
        "REPO_ROOT := $(abspath ../../..)",
        ".PHONY: build run test e2e smoke",
        "",
        "build:",
        '\tbash -lc "source \'$(REPO_ROOT)/scripts/env.sh\' && cargo build --manifest-path Cargo.toml"',
        "",
        "run:",
        f"\tbash -lc \"source '$(REPO_ROOT)/scripts/env.sh' && cargo run --manifest-path Cargo.toml"
        + (f" -- {run_args}\"" if run_args else "\""),
        "",
        "test:",
        '\tbash -lc "source \'$(REPO_ROOT)/scripts/env.sh\' && cargo test --manifest-path Cargo.toml"',
        "",
        "e2e:",
        "\tbash ../e2e/rust-smoke.sh",
        "",
        "smoke:",
        "\tbash ../e2e/rust-smoke.sh baseline" if topic["kind"] == "http_server_router" else "\t$(MAKE) run",
    ]
    return "\n".join(lines) + "\n"


def render_rust_cargo_toml(topic: dict) -> str:
    return text(
        f"""
        [package]
        name = "{project_name(topic, 'rust')}"
        version = "0.1.0"
        edition = "2024"

        [dependencies]
        """
    )


def render_rust_e2e(topic: dict) -> str:
    if topic["kind"] == "http_server_router":
        return text(
            f"""
            #!/usr/bin/env bash
            set -euo pipefail
            MODE="${{1:-mission}}"
            ROOT="$(cd "$(dirname "${{BASH_SOURCE[0]}}")/.." && pwd)"
            PORT="${{PORT:-18080}}"
            export PORT
            pushd "$ROOT/rust" >/dev/null
            make -s --no-print-directory run > /tmp/{topic['slug']}-rust.log 2>&1 &
            pid=$!
            trap 'kill $pid 2>/dev/null || true; wait $pid 2>/dev/null || true' EXIT
            for _ in $(seq 1 40); do
              if curl -fsS "http://127.0.0.1:$PORT/health" > /tmp/{topic['slug']}-rust-health.txt 2>/dev/null; then
                break
              fi
              sleep 0.25
            done
            curl -fsS -X POST --data-binary @"$ROOT/fixtures/echo-body.txt" "http://127.0.0.1:$PORT/echo" > /tmp/{topic['slug']}-rust-echo.txt
            diff -u "$ROOT/fixtures/expected-health.txt" /tmp/{topic['slug']}-rust-health.txt
            diff -u "$ROOT/fixtures/expected-echo.txt" /tmp/{topic['slug']}-rust-echo.txt
            if [ "$MODE" = "mission" ]; then
              status_404="$(curl -s -o /tmp/{topic['slug']}-rust-404.txt -w '%{{http_code}}' "http://127.0.0.1:$PORT/missing")"
              if [ "$status_404" != "404" ]; then
                echo "Mission not complete: expected 404 for unknown route, got $status_404" >&2
                exit 1
              fi
              status_405="$(curl -s -o /tmp/{topic['slug']}-rust-405.txt -w '%{{http_code}}' "http://127.0.0.1:$PORT/echo")"
              if [ "$status_405" != "405" ]; then
                echo "Mission not complete: expected 405 for GET /echo, got $status_405" >&2
                exit 1
              fi
            fi
            popd >/dev/null
            """
        )
    return text(
        f"""
        #!/usr/bin/env bash
        set -euo pipefail
        ROOT="$(cd "$(dirname "${{BASH_SOURCE[0]}}")/.." && pwd)"
        pushd "$ROOT/rust" >/dev/null
        make -s --no-print-directory run > /tmp/{topic['slug']}-rust-out.txt
        if ! diff -u "$ROOT/fixtures/mission-expected.txt" /tmp/{topic['slug']}-rust-out.txt; then
          echo "Mission not complete for Rust: implement the topic until stdout matches fixtures/mission-expected.txt" >&2
          exit 1
        fi
        popd >/dev/null
        """
    )


def rust_struct_code(topic: dict) -> str:
    lines = ["#[derive(Debug, Clone, PartialEq, Eq)]", "pub struct CliArgs {"]
    for option in cli_options(topic):
        lines.append(f"    pub {option['name']}: {rust_scalar_type(option)},")
    lines.append("}")
    return "\n".join(lines)


def rust_run_code(topic: dict) -> str:
    if topic["kind"] == "http_server_router":
        return "\n".join(
            [
                "pub fn run(args: &CliArgs) -> std::io::Result<()> {",
                "    serve(args.port)",
                "}",
            ]
        )
    return "\n".join(
        [
            "pub fn run(args: &CliArgs) -> String {",
            "    let _ = args;",
            f"    {json.dumps(hello_output(topic))}.to_string()",
            "}",
        ]
    )


def rust_lib_code(topic: dict) -> str:
    struct_code = rust_struct_code(topic)
    run_code = rust_run_code(topic)
    if topic["kind"] == "http_server_router":
        http_block = text(
            """
            pub fn serve(port: u16) -> std::io::Result<()> {
                let listener = TcpListener::bind(("127.0.0.1", port))?;
                for stream in listener.incoming() {
                    let mut stream = stream?;
                    handle_connection(&mut stream)?;
                }
                Ok(())
            }

            pub fn response_for(raw: &str) -> String {
                let mut parts = raw.split("\\r\\n\\r\\n");
                let head = parts.next().unwrap_or_default();
                let body = parts.next().unwrap_or_default();
                let mut request = head.lines().next().unwrap_or_default().split_whitespace();
                let method = request.next().unwrap_or_default();
                let path = request.next().unwrap_or_default();
                match (method, path) {
                    ("GET", "/health") => response("200 OK", "ok\\n"),
                    ("POST", "/echo") => response("200 OK", body),
                    ("GET", "/echo") | ("POST", "/health") => response("405 Method Not Allowed", "method-not-allowed\\n"),
                    _ => response("404 Not Found", "not-found\\n"),
                }
            }

            fn handle_connection(stream: &mut TcpStream) -> std::io::Result<()> {
                stream.set_read_timeout(Some(Duration::from_millis(500)))?;
                let mut buffer = Vec::new();
                let mut chunk = [0_u8; 1024];
                loop {
                    match stream.read(&mut chunk) {
                        Ok(0) => break,
                        Ok(size) => {
                            buffer.extend_from_slice(&chunk[..size]);
                            if request_complete(&buffer) || size < chunk.len() {
                                break;
                            }
                        }
                        Err(err) if err.kind() == ErrorKind::WouldBlock || err.kind() == ErrorKind::TimedOut => break,
                        Err(err) => return Err(err),
                    }
                }
                let raw = String::from_utf8_lossy(&buffer);
                let response = response_for(&raw);
                stream.write_all(response.as_bytes())?;
                stream.flush()?;
                Ok(())
            }

            fn request_complete(buffer: &[u8]) -> bool {
                let Some(head_end) = buffer.windows(4).position(|window| window == b"\\r\\n\\r\\n").map(|idx| idx + 4) else {
                    return false;
                };
                let head = String::from_utf8_lossy(&buffer[..head_end]);
                let body_len = head
                    .lines()
                    .find_map(|line| line.strip_prefix("Content-Length: "))
                    .and_then(|value| value.trim().parse::<usize>().ok())
                    .unwrap_or(0);
                buffer.len() >= head_end + body_len
            }

            fn response(status: &str, body: &str) -> String {
                format!(
                    "HTTP/1.1 {status}\\r\\nContent-Length: {}\\r\\nContent-Type: text/plain\\r\\nConnection: close\\r\\n\\r\\n{body}",
                    body.len()
                )
            }
            """
        )
        return "\n".join(
            [
                "use std::io::{ErrorKind, Read, Write};",
                "use std::net::{TcpListener, TcpStream};",
                "use std::time::Duration;",
                "",
                struct_code,
                "",
                run_code,
                "",
                http_block,
            ]
        ) + "\n"
    return f"{struct_code}\n\n{run_code}\n"


def rust_usage(topic: dict) -> str:
    pieces = []
    for option in cli_options(topic):
        label = f"<{option['name']}>" if option.get("required", True) else f"[{option['name']}]"
        pieces.append(label)
    suffix = f" {' '.join(pieces)}" if pieces else ""
    return f"usage: {project_name(topic, 'rust')}{suffix}"


def rust_parse_arg_lines(topic: dict) -> list[str]:
    options = cli_options(topic)
    required_count = sum(1 for option in options if option.get("required", True))
    lines = ["    let argv: Vec<String> = std::env::args().skip(1).collect();"]
    if required_count == 0:
        lines.extend(
            [
                f"    if argv.len() > {len(options)} {{",
                f'        return Err("{rust_usage(topic)}".to_string());',
                "    }",
            ]
        )
    else:
        lines.extend(
            [
                f'    if argv.len() < {required_count} || argv.len() > {len(options)} {{',
                f'        return Err("{rust_usage(topic)}".to_string());',
                "    }",
            ]
        )
    for index, option in enumerate(options):
        name = option["name"]
        rust_type = rust_scalar_type(option)
        display_index = index + 1
        if name == "port":
            lines.extend(
                [
                    "    let port = if let Some(value) = argv.first() {",
                    f'        value.parse::<{rust_type}>().map_err(|_| "argv[{display_index}] must be an integer".to_string())?',
                    "    } else {",
                    '        std::env::var("PORT").ok().and_then(|value| value.parse::<u16>().ok()).unwrap_or(18080)',
                    "    };",
                ]
            )
        elif option["type"] == "int":
            if option.get("required", True):
                lines.append(
                    f'    let {name} = argv[{index}].parse::<{rust_type}>().map_err(|_| "argv[{display_index}] must be an integer".to_string())?;'
                )
            else:
                lines.extend(
                    [
                        f"    let {name} = if let Some(value) = argv.get({index}) {{",
                        f'        value.parse::<{rust_type}>().map_err(|_| "argv[{display_index}] must be an integer".to_string())?',
                        "    } else {",
                        f"        {option['default']}",
                        "    };",
                    ]
                )
        else:
            lines.append(f"    let {name} = argv[{index}].clone();")
    return lines


def rust_main_code(topic: dict) -> str:
    crate_name = project_name(topic, "rust")
    parse_lines = rust_parse_arg_lines(topic)
    if topic["kind"] == "http_server_router":
        run_line = f"    {crate_name}::run(&args)?;"
    else:
        run_line = f'    print!("{{}}", {crate_name}::run(&args));'
    lines = [
        f"fn parse_args() -> Result<{crate_name}::CliArgs, String> {{",
    ]
    lines.extend(parse_lines)
    lines.extend(
        [
            f"    Ok({crate_name}::CliArgs {{",
        ]
    )
    for option in cli_options(topic):
        lines.append(f"        {option['name']},")
    lines.extend(
        [
            "    })",
            "}",
            "",
            "fn main() -> Result<(), Box<dyn std::error::Error>> {",
            "    let args = parse_args().map_err(|message| std::io::Error::new(std::io::ErrorKind::InvalidInput, message))?;",
            run_line,
            "    Ok(())",
            "}",
        ]
    )
    return "\n".join(lines) + "\n"


def render_rust_test(topic: dict) -> str:
    crate_name = project_name(topic, "rust")
    arg_values = []
    for option in cli_options(topic):
        if option["name"] == "port":
            arg_values.append(f"        {option['name']}: {option['default']},")
        elif option["type"] == "int":
            arg_values.append(f"        {option['name']}: {option['default']},")
        else:
            arg_values.append(f"        {option['name']}: {json.dumps(str(option['value']))}.to_string(),")
    if topic["kind"] == "http_server_router":
        return text(
            f"""
            use {crate_name}::response_for;

            #[test]
            fn handles_health_request() {{
                let raw = "GET /health HTTP/1.1\\r\\nHost: localhost\\r\\n\\r\\n";
                let response = response_for(raw);
                assert!(response.contains("200 OK"));
                assert!(response.ends_with("ok\\n"));
            }}
            """
        )
    lines = [
        f"use {crate_name}::{{CliArgs, run}};",
        "",
        "#[test]",
        "fn prints_minimal_template_message() {",
        "    let args = CliArgs {",
    ]
    lines.extend(arg_values)
    lines.extend(
        [
            "    };",
            f"    assert_eq!(run(&args), {json.dumps(hello_output(topic))});",
            "}",
        ]
    )
    return "\n".join(lines) + "\n"
