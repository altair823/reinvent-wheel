#[derive(Debug, Clone, PartialEq, Eq)]
pub struct CliArgs {
    pub input: String,
    pub workers: usize,
}

pub fn run(args: &CliArgs) -> String {
    let _ = args;
    "hello log-analyzer\n".to_string()
}
