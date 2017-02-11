"""
152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Solution: for each point we save both postive and negative while maintaining current max (Came up)
        """
        dp = [[0,nums[0]] if nums[0]<=0 else [nums[0], 0]]
        result = nums[0]

        for i in nums[1:]:
            if i <= 0:
                temp1 = dp[-1][1]*i if dp[-1][1] else 0
                temp2 = dp[-1][0]*i if dp[-1][0] else i
            else:
                temp1 = dp[-1][0]*i if dp[-1][0] else i
                temp2 = dp[-1][1]*i if dp[-1][1] else 0

            dp.append([temp1, temp2])
            result = max(result, temp1)

        return result