"""
448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

Companies 
Google 
"""
# MOWN Solution
# since 1 <= a[i] <= n we can multiply the abs(number at index nums[i]) with -1
# now look for nums < 0

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = abs(nums[idx]) * -1

        return [idx + 1 for idx, num in enumerate(nums) if num > 0]