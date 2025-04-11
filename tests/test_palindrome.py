import unittest
from src.palindrome import is_palindrome

class TestPalindromesSimples(unittest.TestCase):
    
    def test_palindrome_madam(self):
        self.assertTrue(is_palindrome("madam"))
    
    def test_palindrome_racecar(self):
        self.assertTrue(is_palindrome("racecar"))
    
    def test_palindrome_level(self):
        self.assertTrue(is_palindrome("level"))

if __name__ == '__main__':
    unittest.main()
