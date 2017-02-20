"""
280. Wiggle Sort

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

Hide Company Tags Google
Show Tags
Show Similar Problems

"""

# My own solution
class Solution1(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        Solution:
        i even ---> n[i] <= n[i+1]
        i odd  ---> n[i] >= n[i+1]
        """
        for i in range(len(nums)-1):
            if (i % 2 == 0 and nums[i] > nums[i+1]) or (i % 2 != 0 and nums[i] < nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]

# Looked up solution
class Solution2(object):
    def wiggleSort(self, nums):
        for i in range(len(nums)-1):
            nums[i:i+2] = sorted(nums[i:i+2], reverse=i%2)
