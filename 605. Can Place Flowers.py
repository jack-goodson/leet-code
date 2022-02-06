from typing import List

import self as self

'''easy level'''

class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_len: int
        flowerbed_len = len(flowerbed)
        flower_counter: int
        flower_counter = 0
        for pos in range(flowerbed_len):
            if flowerbed_len == 1 and flowerbed[pos] == 0:
                flower_counter +=1
            elif pos == 0:
                if flowerbed[pos] == 0 and flowerbed[pos+1] == 0:
                    flowerbed[pos] = 1
                    flower_counter += 1
            elif pos != 0 and pos != flowerbed_len-1:
                if (flowerbed[pos - 1] == 0) and (flowerbed[pos] == 0) and (flowerbed[pos + 1] == 0):
                    flowerbed[pos] = 1
                    flower_counter += 1
            elif pos == flowerbed_len-1:
                if flowerbed[pos] == 0 and flowerbed[pos-1] == 0:
                    flowerbed[pos] = 1
                    flower_counter += 1
        return flower_counter >= n


Solution.canPlaceFlowers(self, [1,0,0,0,1,0,0], 2)