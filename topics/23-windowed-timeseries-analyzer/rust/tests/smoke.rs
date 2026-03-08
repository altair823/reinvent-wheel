use t23_windowed_timeseries_analyzer_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/series.csv".to_string(),
    };
    assert_eq!(run(&args), "hello timeseries\n");
}
