import unittest
from solution import groupAnagrams

class TestGroupAnagrams(unittest.TestCase):
    def test_basic_case(self): # self refers to the test case instance
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        
        print("\nTESTING BASIC CASE")
        result = groupAnagrams(strs)
        print(result)
        
        # Sort each group and the overall list for consistent comparison
        sorted_result = [sorted(group) for group in result]
        sorted_result.sort()
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        sorted_expected = [sorted(group) for group in expected]
        sorted_expected.sort()
        
        self.assertEqual(sorted_result, sorted_expected)
        
    def test_empty_input(self):
        strs = []
        
        print("\nTESTING EMPTY INPUT")
        result = groupAnagrams(strs)
        print(result)
        
        self.assertEqual(result, [])
        
    def test_single_word(self):
        strs = ["hello"]
        
        print("\nTESTING SINGLE WORD")
        result = groupAnagrams(strs)
        print(result)
        
        self.assertEqual(result, [["hello"]])
        
    def test_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        
        print("\nTESTING NO ANAGRAMS")
        result = groupAnagrams(strs)
        print(result)
        
        # Sort each group and the overall list for consistent comparison
        sorted_result = [sorted(group) for group in result]
        sorted_result.sort()
        expected = [["abc"], ["def"], ["ghi"]]
        sorted_expected = [sorted(group) for group in expected]
        sorted_expected.sort()
        
        self.assertEqual(sorted_result, sorted_expected)

if __name__ == '__main__':
    unittest.main() 