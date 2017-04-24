"""
305. Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the positions?

Hide Company Tags Google
Hide Tags Union Find
Hide Similar Problems (M) Number of Islands

"""
# MOWN: got TLE for this
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        matrix = [[0]*n for i in range(m)]

        total_islands = 0
        islands_list = list()
        for count in range(len(positions)):
            i, j = positions[count]
            matrix[i][j] = count+1

            stack, mapr = list(), dict()
            #print matrix, i, j
            for ti, tj in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                if 0 <= ti < m and 0 <= tj < n:
                    if matrix[ti][tj]:
                        stack.append((ti, tj))
                        mapr[matrix[ti][tj]] = True

            if not stack:
                total_islands += 1

            else:
                total_islands -= len(mapr) -1
                while stack:
                    i, j = stack.pop()
                    matrix[i][j] = count + 1
                    for ti, tj in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                        if 0 <= ti < m and 0 <= tj < n:
                            if matrix[ti][tj] and matrix[ti][tj] != count + 1:  # Bug: Forgot to check if it is already visited
                                stack.append((ti, tj))
            islands_list.append(total_islands)

        return islands_list

# Got TLE for this as well
from collections import defaultdict
class Solution(object):
    def numIslands2(self, m, n, positions):
        # islands_mapr --- Store island_ID as key and list of lands that belong to that island
        # points_mapr -- Store land as key and island_ID that it belong to
        islands_mapr, points_mapr = defaultdict(list), defaultdict()
        result_island, total_islands = list(), 0

        for count in range(len(positions)):
            i, j = positions[count]
            #print i, j
            points_mapr[(i, j)] = count
            islands_mapr[count].append((i, j))
            stack = dict()  # for storing different islands around the current land
            for ti, tj in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                if 0 <= ti < m and 0 <= tj < n:
                    if points_mapr.has_key((ti, tj)):
                        stack[points_mapr[(ti, tj)]] = True

            if len(stack) == 0:
                total_islands += 1

            else:
                total_islands -= len(stack)-1
                for i in stack.keys():
                    islands_mapr[count] += islands_mapr[i]
                    for (ti, tj) in islands_mapr[i]:
                        points_mapr[(ti, tj)] = count
                    islands_mapr.pop(i)

            #print islands_mapr
            result_island.append(total_islands)

        return result_island
