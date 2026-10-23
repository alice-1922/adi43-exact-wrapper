import unittest

from app import greeting


class GreetingTests(unittest.TestCase):
    def test_greets_a_name(self):
        self.assertEqual(greeting("Alice"), "Hello, Alice!")

    def test_ignores_surrounding_whitespace(self):
        self.assertEqual(greeting("  Alice  "), "Hello, Alice!")


if __name__ == "__main__":
    unittest.main()
