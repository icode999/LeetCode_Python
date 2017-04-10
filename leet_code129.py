"""
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

Hide Tags Tree Depth-first Search
Show Similar Problems
"""

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = list()
        for node in [root.left, root.right]:
            if node:
                stack.append([root.val, node])
        if not stack:
            return root.val

        result = list()
        while stack:
            val, node = stack.pop(0)
            temp = list()
            for leaf in [node.left, node.right]:
                if leaf:
                    temp.append([val*10 + node.val, leaf])

            if not temp:
                result.append(val*10 + node.val)
            else:
                stack += temp

        return sum(result)
