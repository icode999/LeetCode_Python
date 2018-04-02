"""
261. Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected,
[0, 1] is the same as [1, 0] and thus will not appear together in edges.

Companies
Google Facebook Zenefits
"""
# MOWN use DFS to detect cycle in undirected graph
from collections import defaultdict
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        self.graph = defaultdict(list)

        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        self.visited = dict()
        count = 0
        for i in range(n):
            if i in self.visited:
                continue

            count += 1  # BUG if there are two disjoint sets [[0, 1], [2, 3]]
            if count > 1 or self.has_cycle(i):
                return False

        return count == 1

    def has_cycle(self, n):
        stack = [[n, -1]]

        while stack:
            current, parent = stack.pop()

            if current in self.visited:
                return True

            self.visited[current] = True
            for node in self.graph[current]:
                if node == parent:
                    continue
                stack.append([node, current])

        return False
