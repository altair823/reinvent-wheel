import unittest

from t21_parallel_log_analyzer_python.core import CliArgs, run


class TopicTests(unittest.TestCase):
    def test_minimal_template_message(self) -> None:
        args = CliArgs(
            input="../fixtures/app.log",
            workers=2,
        )
        self.assertEqual(run(args), "hello log-analyzer\n")


if __name__ == "__main__":
    unittest.main()
