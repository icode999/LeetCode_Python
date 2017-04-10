"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS iterative
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        result = 0
        stack = [root]

        while True:
            temp_s = list()
            result += 1
            while stack:
                troot = stack.pop()
                flag = 0
                for node in [troot.left, troot.right]:
                    if node:
                        temp_s.append(node)
                        flag += 1

                if not flag:
                    return result

            stack = temp_s[:]

# Recursive DFS
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        else:
            depth = map(self.minDepth, [root.left, root.right])
            return 1 + (min(depth) or max(depth))