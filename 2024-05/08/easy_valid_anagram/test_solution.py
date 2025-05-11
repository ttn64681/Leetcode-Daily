import unittest
from solution import isAnagram

# When you write a test class, by inheriting from unittest.TestCase, each test method is a "test case" instance
class TestValidAnagram(unittest.TestCase):
    def test_basic_case(self): # self refers to the test case instance
        print("\nTESTING BASIC CASE")
        result1 = isAnagram("tea", "ate")
        print(result1)
        result2 = isAnagram("racecar", "carract")
        print(result2, end="\n")
        
        self.assertEqual(result1, True) # assertEqual returns True if the two values are equal
        self.assertEqual(result2, False)
        
    def test_empty_strings(self):
        print("\nTESTING EMPTY STRINGS")
        result1 = isAnagram("", "")
        print(result1)
        result2 = isAnagram("", "a")
        print(result2, end="\n")
        
        self.assertEqual(result1, True)
        self.assertEqual(result2, False)
        
    def test_same_string(self):
        print("\nTESTING SAME STRING")
        result1 = isAnagram("hello", "hello")
        print(result1)
        result2 = isAnagram("python", "python")
        print(result2, end="\n")
        
        self.assertEqual(result1, True)
        self.assertEqual(result2, True)
        
    def test_different_lengths(self):
        print("\nTESTING DIFFERENT LENGTHS")
        result1 = isAnagram("short", "longer")
        print(result1)
        result2 = isAnagram("a", "aa")
        print(result2, end="\n")
        
        self.assertEqual(result1, False)
        self.assertEqual(result2, False)

if __name__ == '__main__':
    unittest.main() 