class Solution:
    def intToRoman(self, num: int) -> str:
        # Step 1: Mapping values to symbols (biggest to smallest)
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        res = ""

        # Step 2: Greedy conversion
        for i in range(len(values)):
            # While num is larger, keep subtracting and adding symbol
            while num >= values[i]:
                num -= values[i]
                res += symbols[i]

        return res
