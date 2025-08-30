# THIS CODE TIME COMPLEXITY IS BEST BUT FOR UNDERSTANDING SECOND IS BEST
class Solution:
    def romanToInt(self, s: str) -> int:
        l={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        num=0
        s=s.replace("IV","IIII")
        s=s.replace("IX","VIIII")
        s=s.replace("XL","XXXX")
        s=s.replace("XC","LXXXX")
        s=s.replace("CD","CCCC")
        s=s.replace("CM","DCCCC")

        for char in s:
            num += l[char]
        return num
        
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         # Step 1: Mapping of Roman numerals to integers
#         roman_map = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
        
#         total = 0   # final result
        
#         # Step 2: Traverse the string
#         for i in range(len(s) - 1):
#             # If current value < next value, subtract it
#             if roman_map[s[i]] < roman_map[s[i + 1]]:
#                 total -= roman_map[s[i]]
#             else:
#                 total += roman_map[s[i]]
        
#         # Step 3: Always add the last numeral
#         total += roman_map[s[-1]]
        
#         return total

