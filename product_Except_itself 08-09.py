from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: build prefix array
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # Step 2: build suffix array
        suffix = [1] * n
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        # Step 3: multiply prefix and suffix
        result = [0] * n
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        
        return result
