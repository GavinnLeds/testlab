import unittest
from app import add_numbers


class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
