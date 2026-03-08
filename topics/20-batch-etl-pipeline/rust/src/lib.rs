#[derive(Debug, Clone, PartialEq, Eq)]
pub struct CliArgs {
    pub input: String,
}

pub fn run(args: &CliArgs) -> String {
    let _ = args;
    "hello etl\n".to_string()
}
