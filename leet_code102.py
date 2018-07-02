"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

Hide Company Tags LinkedIn Facebook Amazon Microsoft Apple Bloomberg
Show Tags
Show Similar Problems

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iterative
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = deque([root])
        result = list()
        while True:
            temp_s, temp_result = list(), list()
            while stack:
                troot = stack.popleft()
                temp_result.append(troot.val)
                for node in [troot.left, troot.right]:
                    if node:
                        temp_s.append(node)

            result.append(temp_result)
            if not temp_s:
                return result
            stack = deque(temp_s)

# simplified iterative
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        stack, result = [root], []
        while stack:
            result.append([node.val for node in stack])
            temp = []
            for node in stack:
                temp += [node.left, node.right]

            stack = [node for node in temp if node]

        return result