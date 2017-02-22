"""
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

Hide Company Tags Microsoft
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = list()
        stack = list()
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if len(stack) != 0:
                    root = stack.pop()
                    result.append(root.val)
                    root = root.right
                else:
                    return result