use t03_http_server_router_rust::response_for;

#[test]
fn handles_health_request() {
    let raw = "GET /health HTTP/1.1\r\nHost: localhost\r\n\r\n";
    let response = response_for(raw);
    assert!(response.contains("200 OK"));
    assert!(response.ends_with("ok\n"));
}
