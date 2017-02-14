"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

"""

# Without DP got TLE (Time Limit exceeded) for
'''
[2,20,24,38,44,21,45,48,30,48,14,9,21,10,46,46,12,48,12,38]
48
'''
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0

        result = [nums[0], nums[0]*-1]
        for num in nums[1:]:
            temp = list()
            for tnum in result:
                temp += [tnum+num, tnum-num]
            result = temp[:]
        return result.count(S)

# solution with DP
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        if not nums[0]:
            dp = {nums[0]:2}   # this is a catch that I went wrong (for input [0,0,0,0,0,0,0,0,1]   1)
        else:
            dp = {nums[0]:1, nums[0]*-1:1}

        for num in nums[1:]:
            temp = dict()
            for key in dp.keys():
                for kkey in [key+num, key-num]:
                    if temp.has_key(kkey):
                        temp[kkey] += dp[key]  # make sure you add the dp value (dont increment it by 1)
                    else:
                        temp[kkey] = dp[key]

            dp = temp.copy()
        return dp[S] if dp.has_key(S) else 0
