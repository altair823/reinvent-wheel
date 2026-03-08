use t08_tiny_async_executor_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/tasks.txt".to_string(),
    };
    assert_eq!(run(&args), "hello async\n");
}
