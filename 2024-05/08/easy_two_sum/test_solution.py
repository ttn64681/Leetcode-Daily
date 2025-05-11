import unittest
from solution import two_sum1, two_sum2

# When you write a test class, by inheriting from unittest.TestCase, each test method is a "test case" instance
class TestTwoSum(unittest.TestCase):
    def test_basic_case(self): # self refers to the test case instance
        nums = [2, 7, 11, 15]
        target = 9
        
        print("\nTESTING BASIC CASE")
        result1 = two_sum1(nums, target)
        print(result1)
        result2 = two_sum2(nums, target)
        print(result2, end="\n")
        
        self.assertEqual(sorted(result1), [0, 1]) # assertEqual returns True if the two lists are equal
        self.assertEqual(sorted(result2), [0, 1])
        
    def test_multiple_solutions(self):
        nums = [3, 2, 4, 3]
        target = 6
        
        print("\nTESTING MULTIPLE SOLUTIONS")
        result1 = two_sum1(nums, target)
        print(result1)
        result2 = two_sum2(nums, target)
        print(result2, end="\n")
        
        self.assertEqual(sorted(result1), [1, 2])
        self.assertEqual(sorted(result2), [1, 2])
        
    def test_same_number_twice(self):
        nums = [3, 3]
        target = 6
        
        print("\nTESTING SAME NUMBER TWICE")
        result1 = two_sum1(nums, target)
        print(result1)
        result2 = two_sum2(nums, target)
        print(result2, end="\n")

        self.assertEqual(sorted(result1), [0, 1])
        self.assertEqual(sorted(result2), [0, 1])
        
    def test_no_solution(self):
        nums = [1, 2, 3, 4]
        target = 10
        
        print("\nTESTING NO SOLUTION")
        result1 = two_sum1(nums, target)
        print(result1)
        result2 = two_sum2(nums, target)
        print(result2, end="\n")

if __name__ == '__main__':
    unittest.main() 