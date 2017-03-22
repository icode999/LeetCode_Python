"""
53. Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

Hide Company Tags LinkedIn Bloomberg Microsoft
Hide Tags Array Dynamic Programming Divide and Conquer
Show Similar Problems

"""
# MOWN solution
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        #max_sum_list = [nums[0]]
        maxer = nums[0]
        #temp_max_list = [nums[0]]
        temp_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] + temp_sum < nums[i]:
                #temp_max_list = [nums[i]]
                temp_sum = nums[i]

            else:
                #temp_max_list.append(nums[i])
                temp_sum += nums[i]

            if temp_sum > maxer:
                maxer = temp_sum
                #max_sum_list = temp_max_list[:]

        #print max_sum_list
        return maxer