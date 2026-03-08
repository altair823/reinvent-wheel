use t24_heavy_hitter_stream_rust::{CliArgs, run};

#[test]
fn prints_minimal_template_message() {
    let args = CliArgs {
        input: "../fixtures/events.txt".to_string(),
    };
    assert_eq!(run(&args), "hello heavy-hitter\n");
}
