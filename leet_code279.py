"""
279. Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Hide Company Tags Google
Show Tags
Show Similar Problems

"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int

        Solution: This is a bit tricky, you have get the min of all the perfect square combinations
        So be careful in returning the output  (Came up).

        First time I did a mistake to return the first found combination of perfect squares
        """
        dp = [0, 1]
        if n < 2:
            return dp[n]

        for i in range(2, n+1):
            temp = i
            for j in range(1, i):
                if i < j*j:
                    break
                temp = min(temp, 1+dp[i-(j*j)])

            dp.append(temp)

        #print dp
        return dp[-1]