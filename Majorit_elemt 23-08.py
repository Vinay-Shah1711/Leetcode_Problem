class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candidate=None
        for num in nums:
            if(count==0):
                candidate=num
            if(candidate==num):
                count=count+1
            else:
                count=count-1
        return candidate
        print(candidate)
