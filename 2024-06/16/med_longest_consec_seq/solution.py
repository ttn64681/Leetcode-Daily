from typing import List

class Solution:
    def longestConsecutive(nums: List[int]) -> int:
        numz = set(nums)
        maxFreq = 0

        for num in numz:
            if num-1 not in numz: # if num is start of sequence
                currFreq = 1
                i = 1
                while num+i in numz:
                    currFreq += 1
                    i += 1
                if currFreq > maxFreq: maxFreq = currFreq
        
        return maxFreq
    
if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    print(Solution.longestConsecutive(nums))