"""
107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
Hide Tags Tree Breadth-first Search
Show Similar Problems
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # simplified
        if not root:
            return []

        stack, result = [root], []
        while stack:
            result.append([node.val for node in stack])
            temp = []
            for node in stack:
                temp += [node.left, node.right]

            stack = [node for node in temp if node]

        return result[::-1]

