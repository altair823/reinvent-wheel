fn parse_args() -> Result<t24_heavy_hitter_stream_rust::CliArgs, String> {
    let argv: Vec<String> = std::env::args().skip(1).collect();
    if argv.len() < 1 || argv.len() > 1 {
        return Err("usage: t24_heavy_hitter_stream_rust <input>".to_string());
    }
    let input = argv[0].clone();
    Ok(t24_heavy_hitter_stream_rust::CliArgs {
        input,
    })
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args = parse_args().map_err(|message| std::io::Error::new(std::io::ErrorKind::InvalidInput, message))?;
    print!("{}", t24_heavy_hitter_stream_rust::run(&args));
    Ok(())
}
