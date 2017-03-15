"""
26. Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

Hide Company Tags Microsoft Bloomberg Facebook
Show Tags
Show Similar Problems

"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Own Solution: two pointer, first pointer will point to currnet location where value should be replaced, second pointer moves forward to find next non repetitive num
        """
        if len(nums) < 2:
            return len(nums)

        start, end, current = 1, 1, nums[0]
        while end < len(nums):
            if nums[end] != current:
                current = nums[start] = nums[end]
                start += 1
            end += 1

        return start