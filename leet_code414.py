"""
414. Third Maximum Number

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

Companies
Amazon
"""
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num in res:  # BUG [2, 2, 3, 1]
                continue

            if num > res[2]:
                res[0] = res[1]
                res[1] = res[2]
                res[2] = num

            elif num > res[1]:
                res[0] = res[1]
                res[1] = num

            elif num > res[0]:
                res[0] = num

        return res[0] if res[0] != float('-inf') else max(res)