class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if (numbers[i] + numbers[j] == target):
        #             return[i+1,j+1]

        left,right = 0,len(numbers)-1

        while left < right:
            sum = numbers[left] + numbers[right]

            if(sum == target):
                return [left+1,right+1]
            elif (sum<target):
                left += 1
            elif (sum> target):
                right -= 1
