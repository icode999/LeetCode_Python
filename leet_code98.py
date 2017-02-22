"""
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.


Hide Company Tags Amazon Microsoft Bloomberg Facebook
Show Tags
Show Similar Problems
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# My solution
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Solution: Do a in-order traversal, previous element is always less than current in inorder traversal
        """
        previous = None
        temp_root = root
        stack = list()

        while True:
            if temp_root:
                stack.append(temp_root)
                temp_root = temp_root.left
            else:
                if len(stack) != 0:
                    temp_root = stack.pop()
                    if previous == None:
                        previous = temp_root.val
                    else:
                        if temp_root.val <= previous:
                            return False
                        else:
                            previous = temp_root.val

                    temp_root = temp_root.right
                else:
                    return True
