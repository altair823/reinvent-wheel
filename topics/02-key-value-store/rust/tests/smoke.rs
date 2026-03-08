use t02_key_value_store_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/commands.txt".to_string(),
    };
    assert_eq!(run(&args), "hello kv-store\n");
}
