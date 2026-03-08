from dataclasses import dataclass


@dataclass(frozen=True)
class CliArgs:
    input: str
    workers: int = 2


def run(args: CliArgs) -> str:
    _ = args
    return "hello log-analyzer\n"
