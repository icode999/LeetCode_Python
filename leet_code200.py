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

# My solution
class Solution1(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        Soltion: land and expand, mark the visited blocks
        """
        if not grid:
            return 0
        self.visited = [([False]*len(grid[0]))[:] for i in range(len(grid))]

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not self.visited[i][j]:
                    result += 1  # Everytime we hit a non vistied '1' we mark it as new isalnd starting

                    self.visited[i][j] = True
                    self.sweep(grid, i, j)
        return result

    def sweep(self, grid, i, j):
        for m, n in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
            if 0 <= m < len(grid) and 0 <= n < len(grid[0]):
                if not self.visited[m][n] and grid[m][n] == "1":
                    self.visited[m][n] = True
                    self.sweep(grid, m, n)

# Looked up solution
# No extra space but this modifies the given grid

class Solution2(object):
    def numIslands(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "0"
                map(sink, [i-1, i+1, i, i], [j, j, j-1, j+1])
                return 1
            else:
                return 0
        result = 0
        '''
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += sink(i, j)

        return result
        '''
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[0])))