"""
222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_height = self.getDepth(root.left)
        right_height = self.getDepth(root.right)

        if left_height == right_height:
            return pow(2, left_height) + self.countNodes(root.right)

        else:
            return pow(2, right_height) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0

        result = 0
        while root:
            result += 1
            root = root.left

        return result