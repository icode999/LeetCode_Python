"""
323. Number of Connected Components in an Undirected Graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Companies
Google Twitter

"""
from collections import defaultdict
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        mapr = defaultdict(list)
        for edge in edges:
            mapr[edge[0]].append(edge[1])
            mapr[edge[1]].append(edge[0])

        visited = set()
        result = 0
        for i in range(n):
            if i in visited:
                continue
            result += 1
            stack = [i]

            while stack:
                current = stack.pop()
                if current in visited:
                    continue

                visited.add(current)
                stack += mapr[current]

        return result