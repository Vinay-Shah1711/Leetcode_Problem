class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_=max(candies)
        result=[]
        n=len(candies)
        for i in range (0,n):
            if (candies[i] + extraCandies >= max_):
                result.append(True)
            else:
                result.append(False)
        return result
