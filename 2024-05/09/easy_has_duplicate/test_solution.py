import unittest
from solution import hasDuplicate

class TestHasDuplicate(unittest.TestCase):
    def test_basic_case(self): # self refers to the test case instance
        list = [1, 2, 4, 3, 6, 1]
        
        print("\nTESTING BASIC CASE")
        result = hasDuplicate(list)
        print(result)
        
        self.assertEqual(result, True)
  
if __name__ == '__main__':
    unittest.main() 