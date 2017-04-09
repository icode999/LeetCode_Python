"""
542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1:
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2:
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.

Hide Company Tags Google
Show Tags
"""

# LUP Solution
# Solution: Do a BFS on multiple sources: the squares of the given matrix that have a 0.
# Every time you visit a node, it will be from a path of predecessors that is of shortest distance to a zero.

from collections import deque
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        lenr, lenc = len(matrix), len(matrix[0])
        result = [[0]*lenc for i in range(lenr)]
        que = deque([((row, column), 0) for row in range(lenr) for column in range(lenc) if not matrix[row][column]])
        visited = dict()
        for i in que:
            visited.update({i[0]: True})

        while que:
            (r, c), distance = que.popleft()
            for row, column in self.getNeighbours(r, c, lenr, lenc):
                if not visited.has_key((row, column)):
                    visited.update({(row, column): True})
                    result[row][column] = distance + 1
                    que.append(((row, column), distance+1))
        return result

    def getNeighbours(self, i, j, lenr, lenc):
        for row, column in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
            if 0 <= row < lenr and 0 <= column < lenc:
                yield row, column
