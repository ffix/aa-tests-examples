from tasks.letters_counter import count_letters
import unittest


class TestCountLetters(unittest.TestCase):
    def test_hello_world(self):
        actual = count_letters("Hello world!")
        expected = (10, 2)
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        self.assertEqual(count_letters(""), (0, 0))


if __name__ == "__main__":
    unittest.main()
