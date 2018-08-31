"""
653. Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

Companies
Amazon 6 Google 3
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.mapr = set()
        return self.BFS(root, k)

    def BFS(self, root, k):
        if not root:
            return False

        if k - root.val in self.mapr:
            return True

        self.mapr.add(root.val)
        return self.BFS(root.left, k) or self.BFS(root.right, k)

from Queue import Queue
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        self.mapr = set()
        que = Queue()
        que.put(root)

        while not que.empty():
            node = que.get()
            if k - node.val in self.mapr:
                return True

            self.mapr.add(node.val)
            for tnode in [node.left, node.right]:
                if tnode:
                    que.put(tnode)

        return False