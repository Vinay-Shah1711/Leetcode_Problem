# here we go through at index 1 and check at index 0 value if it is 2 we go till 2nd index and so on 
# and we check our element will go till last element or reach our limit at the ende of list or not if it will go 
# if elemnts limit go till last element return true else false This is jump game I

class Solution:
    def canJump(self, nums: List[int]) -> bool:
            max_reach = 0   # furthest index we can reach so far
            n = len(nums)

            for i in range(n):
                # If the current index is already beyond what we can reach → stuck
                if i > max_reach:
                    return False

                # Update max_reach: how far can we jump from here
                max_reach = max(max_reach, i + nums[i])

                # If we can already reach the last index → win
                if max_reach >= n - 1:
                    return True

            return True


            
