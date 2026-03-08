import unittest

from t18_dataset_profiler_python.core import CliArgs, run


class TopicTests(unittest.TestCase):
    def test_minimal_template_message(self) -> None:
        args = CliArgs(
            input="../fixtures/sample.csv",
        )
        self.assertEqual(run(args), "hello profiler\n")


if __name__ == "__main__":
    unittest.main()
