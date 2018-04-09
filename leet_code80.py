"""
80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.

Companies
Facebook

"""
# MOWN Solution
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype:
        """
        if not nums:
            return 0

        counter = j = 0
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                counter = 1
                nums[j] = nums[i]
                j += 1

            else:
                counter += 1
                if counter <= 2:
                    nums[j] = nums[i]
                    j += 1

        return j