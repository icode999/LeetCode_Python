"""
617.Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# MOWN recursion
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not root1:
            return root2

        root1.val += root2.val if root2 else 0
        if root2:
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

# LUP iterative
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not root1:
            return root2

        result = root1
        stack = [[root1, root2]]
        while stack:
            r1, r2 = stack.pop()
            if not r1 or not r2:
                continue

            r1.val += r2.val if r2 else 0

            if not r1.left:
                r1.left = r2.left if r2.left else None

            else:
                stack.append([r1.left, r2.left])

            if not r1.right:
                r1.right = r2.right if r2.right else None

            else:
                stack.append([r1.right, r2.right])

        return result