"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Companies 
Facebook Microsoft Amazon Bloomberg Uber LinkedIn Apple Airbnb Yelp Yahoo Adobe Dropbox 
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapr = dict()
        for i in range(len(nums)):
            if mapr.has_key(target - nums[i]):
                return [i, mapr[target - nums[i]]]
            else:
                mapr[nums[i]] = i

        return list()