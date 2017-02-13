"""
120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int

        Solutin: We go from bottom up,

                  23                     24
            236        235          245        247
         2364 2361  2351 2358    2451 2458  2478 2473

        we are selecting min of two elements
        """
        if not triangle:
            return 0
        result = triangle[-1]
        for i in range(len(triangle)-2, -1, -1): ### iterate 5,4,3,2,1,0
            for j in range(len(triangle[i])):
                result[j] = triangle[i][j] + min(result[j], result[j+1])

        return result[0]

