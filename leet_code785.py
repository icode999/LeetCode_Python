"""
785. Is Graph Bipartite?

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.
Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.

Companies 
Facebook
"""

# Color the node
# 0: Haven't been colored.
# -1: Blue.
# 1: Red.
# USE DFS
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        self.color_map, self.graph = {}, graph
        for i in range(len(graph)):
            self.color_map[i] = 0

        for i in range(len(graph)):
            if self.color_map[i] == 0: # BUG check if node is visited before doing DFS
                if not self.DFS_Helper(i, 1):
                    return False

        return True

    def DFS_Helper(self, i, color):
        if self.color_map[i] == 0:
            self.color_map[i] = color
            for node in self.graph[i]:

                if not self.DFS_Helper(node, color * -1):
                    return False

        elif self.color_map[i] != color:
            return False

        return True