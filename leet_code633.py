"""
633. Sum of Square Numbers

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: 3
Output: False

"""
# MOWN solution
# Solution: using binary search, increment upper and lower based on summ value
# if summ > num incr upper else incr lower

import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        upper, lower = int(math.sqrt(c)), 0
        while upper >= lower:
            summ = upper ** 2 + lower ** 2
            if summ == c:
                return True

            elif summ > c:
                upper -= 1

            else:
                lower += 1
        return False