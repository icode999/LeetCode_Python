"""
605. Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""


# MOWN solution
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not n:
            return True

        if flowerbed[0] == 0:
            if len(flowerbed) > 1:
                if not flowerbed[1]:
                    flowerbed[0] = 1
                    n = n - 1
            else:
                flowerbed[0] = 1
                n = n - 1
        i = 0
        for i in range(1, len(flowerbed) - 1):
            if not n:
                return True

            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n = n - 1

        if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i + 1] = 0
            n = n - 1

        return True if n < 1 else False