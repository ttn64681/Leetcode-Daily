"""
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.
    
Args:
    nums: List of integers
    target: Target sum to find
        
Returns:
    List of two indices whose corresponding numbers sum to target
"""

# Hash map w/ enumerate
# Time complexity: O(n)
# Space complexity: O(n)
def two_sum1(nums: list[int], target: int) -> list[int]:
    num_map = {}  # val -> index
    
    for i, num in enumerate(nums): # enumerate() returns a tuple (index, value) (immutable) (0, 2), (1, 7), (2, 11), (3, 15)
        complement = target - num
        if complement in num_map:
            return [i, num_map[complement]] # return the index of the complement and the current index
        num_map[num] = i # add the current number and its index to the num_map
    
    # else return an empty list
    return [] 

# Hash map w/o enumerate
# Time complexity: O(n)
# Space complexity: O(n)
def two_sum2(nums: list[int], target: int) -> list[int]:
    num_map = {} # 
    for i in range(len(nums)):
        if target - nums[i] in num_map:
            return [i, num_map[target - nums[i]]]
        num_map[nums[i]] = i
    return []
