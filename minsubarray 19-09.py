# INCOMPLETE TO UNDERSTAND ONLY DOING CODING

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        curr_sum = 0
        res = float("inf")  # initially infinity
        
        for right in range(n):
            curr_sum += nums[right]  # expand window to the right
            
            # shrink window while sum is large enough
            while curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        
        return 0 if res == float("inf") else res
