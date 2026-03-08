use t25_mini_mapreduce_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/documents.txt".to_string(),
    };
    assert_eq!(run(&args), "hello mapreduce\n");
}
