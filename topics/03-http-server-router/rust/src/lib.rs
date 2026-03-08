use std::io::{ErrorKind, Read, Write};
use std::net::{TcpListener, TcpStream};
use std::time::Duration;

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct CliArgs {
    pub port: u16,
}

pub fn run(args: &CliArgs) -> std::io::Result<()> {
    serve(args.port)
}

pub fn serve(port: u16) -> std::io::Result<()> {
    let listener = TcpListener::bind(("127.0.0.1", port))?;
    for stream in listener.incoming() {
        let mut stream = stream?;
        handle_connection(&mut stream)?;
    }
    Ok(())
}

pub fn response_for(raw: &str) -> String {
    let mut parts = raw.split("\r\n\r\n");
    let head = parts.next().unwrap_or_default();
    let body = parts.next().unwrap_or_default();
    let mut request = head.lines().next().unwrap_or_default().split_whitespace();
    let method = request.next().unwrap_or_default();
    let path = request.next().unwrap_or_default();
    match (method, path) {
        ("GET", "/health") => response("200 OK", "ok\n"),
        ("POST", "/echo") => response("200 OK", body),
        ("GET", "/echo") | ("POST", "/health") => response("405 Method Not Allowed", "method-not-allowed\n"),
        _ => response("404 Not Found", "not-found\n"),
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
    let Some(head_end) = buffer.windows(4).position(|window| window == b"\r\n\r\n").map(|idx| idx + 4) else {
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
        "HTTP/1.1 {status}\r\nContent-Length: {}\r\nContent-Type: text/plain\r\nConnection: close\r\n\r\n{body}",
        body.len()
    )
}

