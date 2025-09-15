class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result=[]
        for i in range (len(nums)):
            if (nums[i] != 0):
                result.append(nums[i])
        for i in range (len(nums)):
            if (nums[i] == 0):
                result.append(nums[i])
        
        for i in range(len(nums)):
            nums[i] = result[i]
