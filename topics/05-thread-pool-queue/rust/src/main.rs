fn parse_args() -> Result<t05_thread_pool_queue_rust::CliArgs, String> {
    let argv: Vec<String> = std::env::args().skip(1).collect();
    if argv.len() < 1 || argv.len() > 1 {
        return Err("usage: t05_thread_pool_queue_rust <input>".to_string());
    }
    let input = argv[0].clone();
    Ok(t05_thread_pool_queue_rust::CliArgs {
        input,
    })
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args = parse_args().map_err(|message| std::io::Error::new(std::io::ErrorKind::InvalidInput, message))?;
    print!("{}", t05_thread_pool_queue_rust::run(&args));
    Ok(())
}
