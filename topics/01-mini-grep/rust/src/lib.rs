#[derive(Debug, Clone, PartialEq, Eq)]
pub struct CliArgs {
    pub input: String,
    pub query: String,
}

pub fn run(args: &CliArgs) -> String {
    let _ = args;
    "hello grep\n".to_string()
}
