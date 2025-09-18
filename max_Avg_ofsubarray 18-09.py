class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        window_sum = sum(nums[:k])
        max_avg = window_sum / k

        for i in range (k,n):
            window_sum += nums[i] - nums[i-k]
            max_avg = max(max_avg , window_sum / k)

        return max_avg
