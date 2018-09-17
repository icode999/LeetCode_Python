"""
863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.

Companies
Amazon 2

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# MOWN
# Convert tree to undirected graph
# do DFS or BFS then
from collections import defaultdict


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        mapr = defaultdict(list)
        stack = [root]
        while stack:
            root = stack.pop()
            for node in [root.left, root.right]:
                if node:
                    mapr[root.val].append(node.val)
                    mapr[node.val].append(root.val)
                    stack.append(node)

        result = list()
        visited = set([target.val])
        stack = list()

        if not K and target.val in mapr:
            return [target.val]

        for node in mapr[target.val]:
            stack.append([node, 1])

        while stack:
            node, count = stack.pop()
            visited.add(node)
            if count == K:
                result.append(node)

            for child in mapr[node]:
                if child not in visited:
                    stack.append([child, count + 1])

        return result