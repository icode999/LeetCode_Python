"""
198. House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob = 0
        no_rob = 0

        for num in nums:
            curr_rob = no_rob + num
            no_rob = max(rob,
                         no_rob)  # Bug if we dont rob ith house, no_rob will be max(rob i-1th house, no_rob i-1th house)

            rob = curr_rob
        return max(rob, no_rob)