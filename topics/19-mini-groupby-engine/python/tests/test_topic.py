import unittest

from t19_mini_groupby_engine_python.core import CliArgs, run


class TopicTests(unittest.TestCase):
    def test_minimal_template_message(self) -> None:
        args = CliArgs(
            input="../fixtures/sales.csv",
        )
        self.assertEqual(run(args), "hello groupby\n")


if __name__ == "__main__":
    unittest.main()
