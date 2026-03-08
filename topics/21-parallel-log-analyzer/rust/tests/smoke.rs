use t21_parallel_log_analyzer_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/app.log".to_string(),
        workers: 2,
    };
    assert_eq!(run(&args), "hello log-analyzer\n");
}
