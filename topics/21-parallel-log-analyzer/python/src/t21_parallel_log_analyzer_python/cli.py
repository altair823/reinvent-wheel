import sys

from .core import CliArgs, run


def parse_args(argv: list[str] | None = None) -> CliArgs:
    values = sys.argv[1:] if argv is None else argv
    if len(values) < 1 or len(values) > 2:
        raise SystemExit("usage: python -m t21_parallel_log_analyzer_python.cli <input> [workers]")
    return CliArgs(
        input=values[0],
        workers=int(values[1]) if len(values) > 1 else 2,
    )


def main() -> None:
    print(run(parse_args()), end="")


if __name__ == "__main__":
    main()
