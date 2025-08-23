class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while(i<len(nums)):
            j=i+1
            k=i+2
            while(j<len(nums) and k<len(nums) and nums[i]==nums[j] and nums[j]==nums[k]):
                nums.pop(k)
            i=j
            k=j
        print (len(nums))