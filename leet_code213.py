"""
213. House Robber II

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. 
This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
"""


# Solution house_robber for list[1:] and list[:-1]
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return sum(nums)

        list1 = nums[:-1]
        list2 = nums[1:]

        return max(self.rob_house(list1), self.rob_house(list2))

    def rob_house(self, nums):
        rob, no_rob = 0, 0

        for num in nums:
            current_rob = no_rob + num
            no_rob = max(rob, no_rob)
            rob = current_rob

        return max(rob, no_rob)