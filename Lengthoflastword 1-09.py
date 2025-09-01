class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # for remove space
        s = s.strip()
        n=0
        for ch in reversed(s):
            if ch == " ":
               break
            n += 1
        return n
                