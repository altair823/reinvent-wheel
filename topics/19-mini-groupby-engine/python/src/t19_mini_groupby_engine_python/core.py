from dataclasses import dataclass


@dataclass(frozen=True)
class CliArgs:
    input: str


def run(args: CliArgs) -> str:
    _ = args
    return "hello groupby\n"
