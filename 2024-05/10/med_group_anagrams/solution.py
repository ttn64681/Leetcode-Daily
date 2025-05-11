from typing import List

"""
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Args:
    strs: a List of strings
        
Returns:
    List of Lists of grouped anagram strings
"""

# Hashmap w/ sorted
def groupAnagrams(strs: List[str]) -> List[List[str]]:
     hashmap = {} # hashmap 
     
     for x in strs:
        sortedX = ''.join(sorted(x))
        if sortedX not in hashmap:
            hashmap[sortedX] = [x]
        else:
            hashmap[sortedX].append(x)

     return list(hashmap.values())
    
