"""
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
Hide Company Tags

"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int

        Solution: Go from 2 to n and see how many left childs and right childs and use DP (Came up)
        """
        dp = [1, 1]
        if n < 2:
            return dp[n]

        for i in range(2, n+1):
            count = 0
            for j in range(i):
                count += dp[j]*dp[i-j-1]
            dp.append(count)

        return dp[-1]
