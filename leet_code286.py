"""
286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

Hide Company Tags Google Facebook
Show Tags
Show Similar Problems

"""

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        Solution: Get all the gates and then update neighbours and append neighbours to gates
        """
        gates = [[i , j] for i in range(len(rooms)) for j in range(len(rooms[0])) if rooms[i][j] == 0]
        while gates:
            row, col = gates.pop()
            for nr, nc in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                tr, tc = row + nr, col + nc
                if 0 <= tr < len(rooms) and 0 <= tc < len(rooms[0]) and rooms[tr][tc] not in [0, -1]:
                    if rooms[tr][tc] > 1+rooms[row][col]:
                        rooms[tr][tc] = 1+rooms[row][col]
                        gates.append([tr, tc])