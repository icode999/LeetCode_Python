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

class Solution1(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        Do a level order first and get the height of each node (height is the max depth) and populate dict
        return result by iterating through the dict
        """
        if not root:
            return []

        mapr = dict()
        temp_r = [root]

        temp = list()
        while True:
            for node in temp_r:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

                height = self.get_height(node)
                if mapr.has_key(height):
                    mapr[height].append(node.val)
                else:
                    mapr[height] = [node.val]

            if not temp:
                break
            temp_r = temp[:]
            temp = list()

        keyr = mapr.keys()
        keyr.sort()
        result = [mapr[key] for key in keyr]
        return result

    def get_height(self, node):
        if not node:
            return 0

        if not node.right and not node.left:
            return 1

        else:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))