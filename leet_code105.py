"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

Companies
Bloomberg

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# LUP Solution
# https://articles.leetcode.com/construct-binary-tree-from-inorder-and-preorder-postorder-traversal/

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        in_order_idx = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        left_pre_start, left_pre_end = 1, in_order_idx + 1
        right_pre_start, right_pre_end = in_order_idx + 1, len(preorder)

        left_in_start, left_in_end = 0, in_order_idx
        right_in_start, right_in_end = in_order_idx + 1, len(inorder)

        root.left = self.buildTree(preorder[left_pre_start: left_pre_end], inorder[left_in_start: left_in_end])
        root.right = self.buildTree(preorder[right_pre_start: right_pre_end], inorder[right_in_start: right_in_end])

        return root