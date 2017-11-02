
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

"""
# MOWN Solution got TLE
# Solution: Start from the end and maintain DP to store if we can reach end index from that index (GOT TLE)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.dp = [False] * len(nums)
        if not self.dp:
            return True
        else:
            self.dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            self.Helper(nums, i)

        return self.dp[0]

    def Helper(self, nums, position):
        if position + nums[position] >= len(nums):
            self.dp[position] = True
            return True

        for j in range(1, nums[position] + 1):
            if self.dp[position + j]:
                self.dp[position] = True
                return True

        return False

# LUP o(n) time and const space
# start from end and save the last know index from where you can reach the end
# now compare that check if diff between that last known index and current index is less than the value
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_known = len(nums)-1 if len(nums) else 0
        for i in range(len(nums)-2, -1, -1):
            last_known = i if last_known-i <= nums[i] else last_known
        return True if last_known == 0 else False