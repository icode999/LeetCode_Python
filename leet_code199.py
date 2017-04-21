"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

Credits:
Special thanks to @amrsaqr for adding this problem and creating all test cases.

Hide Company Tags Amazon
Hide Tags Tree Depth-first Search Breadth-first Search
Hide Similar Problems (M) Populating Next Right Pointers in Each Node (M) Boundary of Binary Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution: BFS level order iterative
# MOWN BFS

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return list()
        result = list()
        listr = [root]

        while True:
            tempr = list()
            for node in listr:
                for tnode in [node.left, node.right]:
                    if tnode:
                        tempr.append(tnode)
            result.append(node.val)
            if tempr:
                listr = tempr[:]
            else:
                break

        return result

# MOWN  DFS

from collections import defaultdict
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return list()
        mapr, stack, troot, counter = defaultdict(), list(), root, 0
        while True:
            if troot:
                counter += 1
                stack.append([troot, counter])
                troot = troot.left
            else:
                if stack:
                    troot, counter = stack.pop()
                    mapr[counter], troot = troot.val, troot.right
                else:
                    break

        return map(lambda i: mapr[i], sorted(mapr.keys()))