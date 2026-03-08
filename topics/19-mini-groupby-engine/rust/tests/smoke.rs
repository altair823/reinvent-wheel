use t19_mini_groupby_engine_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/sales.csv".to_string(),
    };
    assert_eq!(run(&args), "hello groupby\n");
}
