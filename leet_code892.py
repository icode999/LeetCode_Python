"""
892. Surface Area of 3D Shapes

On a N * N grid, we place some 1 * 1 * 1 cubes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).\
Return the total surface area of the resulting shapes.


Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Note:

1 <= N <= 50
0 <= grid[i][j] <= 50

"""
# MOWN
# Add sentinel row and columns on all 4 sides
# for each cell in grid, check neighbours and add diff to result
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid.insert(0, [0] * len(grid[0]))
        grid.append([0] * len(grid[0]))

        for i in range(len(grid)):
            grid[i].insert(0, 0)
            grid[i].append(0)

        result = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                neighbours = [[i, j - 1], [i, j + 1], [i - 1, j], [i + 1, j]]
                if grid[i][j] != 0:
                    for ni, nj in neighbours:
                        temp = grid[i][j] - grid[ni][nj]
                        if temp > 0:
                            result += temp

                    result += 2

        return result