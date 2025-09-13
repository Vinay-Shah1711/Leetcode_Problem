class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        last = len(flowerbed) - 1

        for i in range(len(flowerbed)):   # check full flowerbed, not just last-1
            if flowerbed[i] == 0:
                # check left and right safely
                if (i == 0 or flowerbed[i-1] == 0) and (i == last or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n -= 1

            if n <= 0:
                return True

        return False


# THIS APPROACH IS GOOD BUT IN LONGER RUN NOT GOOD SO ABOVE TRICK IS LEFT AND RIGHT CHECK

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         last=len(flowerbed)-1
#         for i in range(last):
            
#             if (flowerbed[0] == 0):
#                 if(flowerbed[1] == 0):
#                     flowerbed[0] = 1
#                     n=n-1

#             if (flowerbed[last] == 0):
#                 if(flowerbed[last-1] == 0):
#                     flowerbed[last] = 1
#                     n=n-1

#             if (flowerbed[i] == 0):
#                 if(flowerbed[i+1] == 0 and flowerbed[i-1] == 0):
#                     flowerbed[i] = 1
#                     n = n-1
                
#         if(n<=0):
#             return True
#         else:
#             return False
        
