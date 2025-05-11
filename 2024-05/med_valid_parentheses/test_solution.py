import unittest
from solution import is_valid

class TestValidParentheses(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(is_valid("()"))
        self.assertTrue(is_valid("()[]{}"))
        
    def test_nested_valid(self):
        self.assertTrue(is_valid("([{}])"))
        self.assertTrue(is_valid("{[]}"))
        
    def test_invalid_cases(self):
        self.assertFalse(is_valid("(]"))
        self.assertFalse(is_valid("([)]"))
        self.assertFalse(is_valid("]"))
        
    def test_empty_string(self):
        self.assertTrue(is_valid(""))
        
    def test_unmatched_open(self):
        self.assertFalse(is_valid("("))
        self.assertFalse(is_valid("(["))

if __name__ == '__main__':
    unittest.main() 