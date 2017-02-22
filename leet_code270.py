"""
270. Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

Hide Company Tags Microsoft Google Snapchat
Show Tags
Show Similar Problems
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        result = [None, float('inf')]

        while root:
            if root.val > target:
                if root.val-target < result[1]:
                    result = [root.val, root.val-target]
                root = root.left

            elif root.val < target:
                if target-root.val < result[1]:
                    result = [root.val, target-root.val]
                root = root.right

            else:
                return root.val

        return result[0]