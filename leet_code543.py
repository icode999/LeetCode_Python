"""
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

Hide Company Tags Google Facebook
Show Tags


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# LUP
# Solution: max diameter can start from any node in the entire tree, so @ everynode we find max depth at the same time we get max diameter

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.get_max_depth(root)
        return self.result

    def get_max_depth(self, troot):
        if not troot:
            return 0
        l_len =self.get_max_depth(troot.left)
        r_len = self.get_max_depth(troot.right)
        self.result = max(self.result, l_len+r_len)
        return 1 + max(l_len , r_len)

