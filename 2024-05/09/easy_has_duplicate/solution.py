from typing import List

"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Args: 
    nums a List of integers
    
Returns:
    True if nums contains a duplicate integer, False if otherwise

"""

# Hasmap
def hasDuplicate(nums: List[int]) -> bool:
     array = []

     for i in nums:
         if i not in array:
             array.append(i)
         else:
             return True
     return False  