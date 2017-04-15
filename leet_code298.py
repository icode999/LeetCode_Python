"""
298. Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.


Hide Company Tags Google
Hide Tags Tree
Hide Similar Problems (H) Longest Consecutive Sequence (M) Binary Tree Longest Consecutive Sequence II
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# MOWN
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            stack, maxer = [[1, root]], 0
        else:
            return 0

        while stack:
            length, current = stack.pop()
            maxer = max(maxer, length)

            for node in [current.left, current.right]:
                if node:
                    if node.val == current.val + 1:
                        stack.append([length+1, node])
                    else:
                        stack.append([1, node])
        return maxer
