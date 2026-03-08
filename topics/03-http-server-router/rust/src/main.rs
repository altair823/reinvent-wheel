fn parse_args() -> Result<t03_http_server_router_rust::CliArgs, String> {
    let argv: Vec<String> = std::env::args().skip(1).collect();
    if argv.len() > 1 {
        return Err("usage: t03_http_server_router_rust [port]".to_string());
    }
    let port = if let Some(value) = argv.first() {
        value.parse::<u16>().map_err(|_| "argv[1] must be an integer".to_string())?
    } else {
        std::env::var("PORT").ok().and_then(|value| value.parse::<u16>().ok()).unwrap_or(18080)
    };
    Ok(t03_http_server_router_rust::CliArgs {
        port,
    })
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args = parse_args().map_err(|message| std::io::Error::new(std::io::ErrorKind::InvalidInput, message))?;
    t03_http_server_router_rust::run(&args)?;
    Ok(())
}
