"""
285. Inorder Successor in BST

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

Companies
Facebook Microsoft Pocket Gems

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# MOWN indorder traversal
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root or not p:
            return None

        current = root
        stack = list()
        flag = False

        while current or stack:
            if current:
                stack.append(current)
                current = current.left

            else:
                if stack:
                    current = stack.pop()
                    if flag:
                        return current
                    elif current == p:
                        flag = True

                    current = current.right

        return None