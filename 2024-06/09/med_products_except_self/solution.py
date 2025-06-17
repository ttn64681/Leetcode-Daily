from typing import List

class Solution:
    def productExceptSelf(nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        prefix = 1
        for i in range(n): # left-right prefix
            res[i] *= prefix
            prefix *= nums[i]
            print(prefix)
        print(res)

        suffix = 1
        for i in range(n-1, -1, -1): # right-left suffix
            res[i] *= suffix
            suffix *= nums[i]
            print(suffix)
        print(res)
        
        return res

if __name__ == "__main__":
    nums = [-1,0,1,2,3]
    print(Solution.productExceptSelf(nums))