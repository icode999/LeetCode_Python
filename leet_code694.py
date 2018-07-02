"""
694. Number of Distinct Islands

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.


Companies
Amazon
"""
# MOWN with bug

from collections import defaultdict
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        neighbours = [[0, -1, 'l'], [-1, 0, 'u'], [0, 1, 'r'], [1, 0, 'd']]
        result = defaultdict(int)

        def DFSHelper(stack):
            string = ""
            while stack:
                i, j, direction = stack.pop()

                if direction == 'b':
                    string += direction
                    continue


                string += direction
                grid[i][j] = 0

                stack.append([None, None, 'b'])  # bug [[1,1,0],[0,1,1],[0,0,0],[1,1,1],[0,1,0]]
                # If we dont add the end (b) we get same pattern for both islands (ORDR and ORDR)

                for ni, nj, tdirection in neighbours:
                    if 0 <= i + ni < len(grid) and 0 <= j + nj < len(grid[0]) and grid[ni + i][nj + j] == 1:
                        stack.append([ni + i, nj + j, tdirection])

            return string

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    string = DFSHelper([[i, j, 'o']])
                    result[string] += 1

        return len(result)
