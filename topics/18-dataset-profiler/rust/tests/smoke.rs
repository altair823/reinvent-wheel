use t18_dataset_profiler_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/sample.csv".to_string(),
    };
    assert_eq!(run(&args), "hello profiler\n");
}
