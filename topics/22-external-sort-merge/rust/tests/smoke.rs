use t22_external_sort_merge_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/numbers.txt".to_string(),
    };
    assert_eq!(run(&args), "hello sort\n");
}
