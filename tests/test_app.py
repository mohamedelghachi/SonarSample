import sys
import os
import unittest

# Add the project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import add, is_palindrome

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("Engage le jeu que je le gagne"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("chatgpt"))

if __name__ == "__main__":
    unittest.main()
