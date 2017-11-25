"""
516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

Companies 
Amazon Uber 

"""
# LUP Solution
# use 2D DP, (x, y) means max plain string between index x to index y
# iterate through length 2 to len(s) and cal max plain string available for each string length
# TLE

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [[1] * len(s) for i in range(len(s))]

        for length in range(2, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = length - 1 + i

                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = 2

                    else:
                        dp[i][j] = 2 + dp[i + 1][j - 1]

                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][len(s) - 1]