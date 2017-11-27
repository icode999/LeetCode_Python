"""
366. Find Leaves of Binary Tree

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree
          1
         / \
        2   3
       / \
      4   5
Returns [4, 5, 3], [2], [1].

Explanation:
1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         /
        2
2. Now removing the leaf [2] would result in this tree:

          1
3. Now removing the leaf [1] would result in the empty tree:

          []
Returns [4, 5, 3], [2], [1].

Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.

Hide Company Tags LinkedIn
Show Tags


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# LUP
# Build a map {depth: [list of nodes]} then iterate through that map and populate result
from collections import defaultdict
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.mapr = defaultdict(list)
        self.build_height_map(root)

        keys = self.mapr.keys()
        keys.sort()

        result = list()
        for key in keys:
            result.append(self.mapr[key])

        return result

    def build_height_map(self, root):
        if not root:
            return 0

        left = self.build_height_map(root.left)
        right = self.build_height_map(root.right)

        self.mapr[max(left, right) + 1].append(root.val)
        return max(left, right) + 1