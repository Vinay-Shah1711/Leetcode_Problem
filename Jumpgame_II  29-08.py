class Solution:
    def jump(self, nums: List[int]) -> int:
        jump=0
        farthest=0
        end=0
        n=len(nums)

        for i in range(n-1):
            farthest=max(farthest,i+nums[i])

            if i==end:
                jump += 1
                end=farthest
        return jump