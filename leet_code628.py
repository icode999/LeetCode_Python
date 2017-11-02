"""
628. Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24

Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

"""
# Solution: Maintain max and min 3 element list and return max(ma1*ma2*ma3 or ma3*mi1*mi2)
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_list, min_list = list(), list()
        for num in nums:
            if len(max_list) < 3:
                max_list.append(num)

            elif min(max_list) < num:
                max_list.remove(min(max_list))
                max_list.append(num)

            if len(min_list) < 3:
                min_list.append(num)

            elif max(min_list) > num:
                min_list.remove(max(min_list))
                min_list.append(num)

        min_list.sort()
        max_list.sort()

        return max(max_list[0] * max_list[1] * max_list[2], max_list[2] * min_list[0] * min_list[1])