import unittest

from t23_windowed_timeseries_analyzer_python.core import CliArgs, run


class TopicTests(unittest.TestCase):
    def test_minimal_template_message(self) -> None:
        args = CliArgs(
            input="../fixtures/series.csv",
        )
        self.assertEqual(run(args), "hello timeseries\n")


if __name__ == "__main__":
    unittest.main()
