"""
463. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:

Hide Company Tags Google
Hide Tags Hash Table
"""

# MOWN solution with 2 bugs
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result, flag = 0, False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    flag = True
                    break
            # bug 1 break first for loop a well
            if flag:
                break

        if not flag:
            return result

        stack = [[i, j]]
        while stack:
            ci, cj = stack.pop()
            # bug 2: Need to check if a cell is already visited
            if grid[ci][cj] == 'V':
                continue

            grid[ci][cj] = 'V'
            for ni, nj in [[ci-1, cj], [ci+1, cj], [ci, cj-1], [ci, cj+1]]:
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    if grid[ni][nj] == 1:
                        stack.append([ni, nj])
                    elif grid[ni][nj] == 0:
                        result += 1
                else:
                    result += 1
        return result

