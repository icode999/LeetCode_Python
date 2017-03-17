"""
361. Bomb Enemy

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
Credits:
Special thanks to @memoryless for adding this problem and creating all test cases.

Hide Company Tags Google
Show Tags
"""

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        Solution: build a 2D dp and count all enemies (by reading each row left to right and right to left
        and reading each column left to right anf right to left and figure out max)
        """
        if not grid:
            return 0

        maxer = 0
        dp = [[0]*len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            count = 0
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    dp[i][j] += count
                elif grid[i][j] == 'E':
                    count += 1
                else:
                    count = 0

            count = 0
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] == '0':
                    dp[i][j] += count
                elif grid[i][j] == 'E':
                    count += 1
                else:
                    count = 0

        for j in range(len(grid[0])):
            count = 0
            for i in range(len(grid)):
                if grid[i][j] == '0':
                    dp[i][j] += count
                elif grid[i][j] == 'E':
                    count += 1
                else:
                    count = 0
            count = 0
            for i in range(len(grid)-1, -1, -1):
                if grid[i][j] == '0':
                    dp[i][j] += count
                    if dp[i][j] > maxer:
                        maxer = dp[i][j]
                elif grid[i][j] == 'E':
                    count += 1
                else:
                    count = 0
        return maxer