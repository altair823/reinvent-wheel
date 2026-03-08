import unittest

from t25_mini_mapreduce_python.core import CliArgs, run


class TopicTests(unittest.TestCase):
    def test_minimal_template_message(self) -> None:
        args = CliArgs(
            input="../fixtures/documents.txt",
        )
        self.assertEqual(run(args), "hello mapreduce\n")


if __name__ == "__main__":
    unittest.main()
