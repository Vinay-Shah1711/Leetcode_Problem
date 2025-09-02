class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is empty, return 0
        if not needle:
            return 0
        
        # Loop over haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Check if substring from i matches needle
            if haystack[i:i+len(needle)] == needle:
                return i
        
        # If not found
        return -1

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)
