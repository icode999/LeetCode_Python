"""
515. Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# MOWN BFS
from collections import deque
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return list()

        row = deque([root, 'end'])
        result, cmax = list(), None

        while row:
            current_node = row.popleft()
            if current_node == 'end':
                if row:
                    row.append('end')
                result.append(cmax)
                cmax = None
                continue

            cmax = max(cmax, current_node.val) if cmax != None else current_node.val
            for node in [current_node.left, current_node.right]:
                if node:
                    row.append(node)
        return result


# MOWN BFS
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        row = [root] if root else list()
        result = list()

        while row:
            result.append(max(node.val for node in row))
            row = [node for tnode in row for node in [tnode.left, tnode.right] if node]
        return result