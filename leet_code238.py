"""
238. Product of Array Except Self

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

"""
# LUP solution
# Iterate from start and append to result the product of all numbers so far
# Iterate from back and multiply all numbers from back exculding it

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result, temp = list(), 1
        for num in nums:
            result.append(temp)
            temp *= num

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= temp
            temp *= nums[i]

        return result