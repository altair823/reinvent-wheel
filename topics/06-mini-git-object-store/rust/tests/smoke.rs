use t06_mini_git_object_store_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/blob.txt".to_string(),
    };
    assert_eq!(run(&args), "hello git-object\n");
}
