"""
501. Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

Companies
Google

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# LUP
# Do inorder iterative
# Since all the same nodes are connected, we count occurance of each node and save the current max and mode

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        mode, maxcount, current_val, count = [], 0, None, 0
        stack, current = list(), root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if current.val == current_val:
                count += 1

            else:
                current_val = current.val
                count = 1

            if count == maxcount:
                mode.append(current_val)

            elif count > maxcount:
                mode = [current_val]
                maxcount = count

            current = current.right

        return mode
