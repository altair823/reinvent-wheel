fn parse_args() -> Result<t01_mini_grep_rust::CliArgs, String> {
    let argv: Vec<String> = std::env::args().skip(1).collect();
    if argv.len() < 2 || argv.len() > 2 {
        return Err("usage: t01_mini_grep_rust <input> <query>".to_string());
    }
    let input = argv[0].clone();
    let query = argv[1].clone();
    Ok(t01_mini_grep_rust::CliArgs {
        input,
        query,
    })
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args = parse_args().map_err(|message| std::io::Error::new(std::io::ErrorKind::InvalidInput, message))?;
    print!("{}", t01_mini_grep_rust::run(&args));
    Ok(())
}
