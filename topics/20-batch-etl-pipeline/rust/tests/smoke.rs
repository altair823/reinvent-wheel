use t20_batch_etl_pipeline_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/raw.csv".to_string(),
    };
    assert_eq!(run(&args), "hello etl\n");
}
