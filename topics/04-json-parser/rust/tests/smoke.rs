use t04_json_parser_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/sample.json".to_string(),
    };
    assert_eq!(run(&args), "hello json\n");
}
