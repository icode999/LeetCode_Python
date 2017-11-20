"""
367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""

# LUP perfect square = 1 + 3 + 5 + 7 + ...
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        square, i = 0, 1

        while square <= num:
            if square == num:
                return True

            square += i
            i += 2

        return False