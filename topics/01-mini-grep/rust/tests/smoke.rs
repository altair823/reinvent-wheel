use t01_mini_grep_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/sample.txt".to_string(),
        query: "Rust".to_string(),
    };
    assert_eq!(run(&args), "hello grep\n");
}
