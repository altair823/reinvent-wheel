import unittest

from t22_external_sort_merge_python.core import CliArgs, run


class TopicTests(unittest.TestCase):
    def test_minimal_template_message(self) -> None:
        args = CliArgs(
            input="../fixtures/numbers.txt",
        )
        self.assertEqual(run(args), "hello sort\n")


if __name__ == "__main__":
    unittest.main()
