fn parse_args() -> Result<t21_parallel_log_analyzer_rust::CliArgs, String> {
    let argv: Vec<String> = std::env::args().skip(1).collect();
    if argv.len() < 1 || argv.len() > 2 {
        return Err("usage: t21_parallel_log_analyzer_rust <input> [workers]".to_string());
    }
    let input = argv[0].clone();
    let workers = if let Some(value) = argv.get(1) {
        value.parse::<usize>().map_err(|_| "argv[2] must be an integer".to_string())?
    } else {
        2
    };
    Ok(t21_parallel_log_analyzer_rust::CliArgs {
        input,
        workers,
    })
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args = parse_args().map_err(|message| std::io::Error::new(std::io::ErrorKind::InvalidInput, message))?;
    print!("{}", t21_parallel_log_analyzer_rust::run(&args));
    Ok(())
}
