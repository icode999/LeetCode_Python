"""
226. Invert Binary Tree

Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you cant invert a binary tree on a whiteboard so fuck off.
Hide Tags Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        temp = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(temp)
        return root

# BFS iterative
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        stack = [root]

        while True:
            temp = list()
            for node in stack:
                node.left, node.right = node.right, node.left
                for cnode in [node.left, node.right]:
                    if cnode:
                        temp.append(cnode)
            if temp:
                stack = temp[:]
            else:
                return root

# BFS iterative simple (LUP)
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right

        return root