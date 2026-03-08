import unittest

from t20_batch_etl_pipeline_python.core import CliArgs, run


class TopicTests(unittest.TestCase):
    def test_minimal_template_message(self) -> None:
        args = CliArgs(
            input="../fixtures/raw.csv",
        )
        self.assertEqual(run(args), "hello etl\n")


if __name__ == "__main__":
    unittest.main()
