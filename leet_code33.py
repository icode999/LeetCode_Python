"""
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Hide Company Tags LinkedIn Bloomberg Uber Facebook Microsoft
Show Tags
Show Similar Problems

"""

# OWN Soultion
# Solution: devide and conquer, if we see that nums[low] > nums[high] there is rotation in that part, so we devide the list as low:pivot and pivot+1:high and do 2 Binary search for each part recursively

# if nums[low] < nums[high] there is no rotation so we just do regular binary search
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        low = 0
        high = len(nums) - 1

        return self.binary_search(nums, low, high, target)

    def binary_search(self, nums, low, high, target):
        pivot = (low + high)/2
        if low == high:
            return low if nums[low] == target else -1

        if nums[low] > nums[high]:
            bs1 = self.binary_search(nums, low, pivot, target)
            if pivot != high:
                bs2 = self.binary_search(nums, pivot+1, high, target)

            if bs1 != -1:
                return bs1
            else:
                return bs2

        if nums[low] < nums[high]:
            if target == nums[pivot]:
                return pivot

            elif nums[pivot] < target:
                return self.binary_search(nums, pivot+1, high, target)

            else:
                return self.binary_search(nums, low, pivot, target)
