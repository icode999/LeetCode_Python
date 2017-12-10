"""
442. Find All Duplicates in an Array

Given an array of integers, 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

Companies 
Pocket Gems 
"""
# MOWN solution
# add 0.1 to nums at index nums[i]
# for num that is repeated twice will have 0.2, so compare each num with its int version and see if diff is > 0.15
# reason we are looking for 0.15 instead of 0.2 is
# >>> num = 2.2
# >>> num-int(num)
# 0.20000000000000018

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = list()

        for i in range(len(nums)):
            idx = int(nums[i]) - 1
            nums[idx] += 0.1

        return [idx + 1 for idx, num in enumerate(nums) if num - int(num) > 0.15]