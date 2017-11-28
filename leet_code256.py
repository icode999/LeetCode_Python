"""
256. Paint House

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. 
The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 
For example, costs[0][0] is the cost of painting house 0 with color red; 
costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Companies 
LinkedIn 

"""
# LUP
# at each house we check what is the min cost to apply a particular paint
# at the end of last house we check what is min cost out of all the paints

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        dp = [[0] * len(costs[0]) for i in range(len(costs))]
        dp[0] = costs[0]

        for i in range(1, len(costs)):
            dp[i][0] = min(dp[i - 1][1:]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][:2]) + costs[i][2]

        return min(dp[-1])