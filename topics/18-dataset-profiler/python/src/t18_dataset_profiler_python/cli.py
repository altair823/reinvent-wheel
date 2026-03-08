import sys

from .core import CliArgs, run


def parse_args(argv: list[str] | None = None) -> CliArgs:
    values = sys.argv[1:] if argv is None else argv
    if len(values) < 1 or len(values) > 1:
        raise SystemExit("usage: python -m t18_dataset_profiler_python.cli <input>")
    return CliArgs(
        input=values[0],
    )


def main() -> None:
    print(run(parse_args()), end="")


if __name__ == "__main__":
    main()
