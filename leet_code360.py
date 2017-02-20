"""
360. Sort Transformed Array

Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]
Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.

Hide Company Tags Google
Show Tags

"""
# Looked up Solution
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]

        Solution:  This is parabola problem where result depends of if a>=0 or a < 0
        example:

        x = [-3, -2, -1, 0, 1, 2, 3]
        y = [13, 5, 1, 1, 5, 13, 25]   ---- a > 0  (a = 2)
            [-5, -3, -1, 1, 3, 5, 7]   ---- a = 0
            [-23, -11, -3, 1, 1, -3, -11] - a < 0 (a = -2)


        So for a >= 0 edges are higher than center, hence we have to start populating result from the end depending on which edge have max value

        for a < 0 edges will be smaller than center, hence we have to start populating result from the start depending on which edge have min value

        """
        nums = [a*i*i+b*i+c for i in nums]
        pointer1, pointer2 = 0, len(nums)-1

        result = [None]*len(nums)
        digit, pointer = (1, pointer1) if a < 0 else (-1, pointer2)
        while pointer1 <= pointer2:
            if digit*nums[pointer1] < digit*nums[pointer2]:
                result[pointer] = nums[pointer1]
                pointer1 += 1
            else:
                result[pointer] = nums[pointer2]
                pointer2 -= 1

            pointer += digit

        return result



