import unittest

from t24_heavy_hitter_stream_python.core import CliArgs, run


class TopicTests(unittest.TestCase):
    def test_minimal_template_message(self) -> None:
        args = CliArgs(
            input="../fixtures/events.txt",
        )
        self.assertEqual(run(args), "hello heavy-hitter\n")


if __name__ == "__main__":
    unittest.main()
