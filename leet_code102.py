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

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        stack = [root]
        result = list()

        while True:
            tstack, tresult = list(), list()
            for node in stack:
                tresult.append(node.val)
                for tnode in [node.left, node.right]:
                    if tnode:
                        tstack.append(tnode)

            result.append(tresult)  # remember to do this always before we break the loop
            if not tstack:
                break
            stack = tstack[:]

        return result