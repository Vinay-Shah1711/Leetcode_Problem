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

            