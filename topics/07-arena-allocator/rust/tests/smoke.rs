use t07_arena_allocator_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/words.txt".to_string(),
    };
    assert_eq!(run(&args), "hello arena\n");
}
