class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(c in it for c in s)

sol = Solution()

print(sol.isSubsequence("abc", "ahbgdc"))   # Example 1
print(sol.isSubsequence("axc", "ahbgdc"))   # Example 2
print(sol.isSubsequence("ace", "abcde"))    # Example 3
print(sol.isSubsequence("aec", "abcde"))    # Example 4
print(sol.isSubsequence("", "abcde"))       # Example 5 (empty string case)
print(sol.isSubsequence("abc", ""))         # Example 6
