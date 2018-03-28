"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

Hide Company Tags Amazon Microsoft Google Facebook Zenefits
Show Tags
Show Similar Problems

"""

# MOWN
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result += 1
                    stack = [[i, j]]
                    while stack:
                        ti, tj = stack.pop()
                        grid[ti][tj] = "0"

                        for ni, nj in [[ti - 1, tj], [ti + 1, tj], [ti, tj - 1], [ti, tj + 1]]:
                            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == "1":
                                stack.append([ni, nj])
        return result
