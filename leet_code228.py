"""
221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

Hide Company Tags Apple Airbnb Facebook
Hide Tags Dynamic Programming
Hide Similar Problems (H) Maximal Rectangle

"""
# LUP dp[iu][j] represents the length of the square
# whose lower-right corner is located at (i, j)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        dp, maxer = [[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)], 0
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1]=='1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    maxer = max(maxer, dp[i][j])

        return maxer*maxer
