"""
739. Daily Temperatures

Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have
to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

Companies 
Google 
"""

# MOWN solution after doing Next Greater num
# Iterate through the nums list, Use stack to save all the descending sub sequence of numbers from nums
# everytime you hit higher number, that will the greatest number for the nums in stack that are,
# less than the number (so we pop all of them out
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack, result = list(), [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][-1] < temp:
                tidx, ttemp = stack.pop()
                result[tidx] = idx - tidx

            stack.append([idx, temp])

        return result