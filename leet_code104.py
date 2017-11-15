"""
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Hide Company Tags LinkedIn Uber Apple Yahoo
Show Tags
Show Similar Problems

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

# Iterative BFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        result = 1
        nodes_list = [root]

        temp_l = list()
        while True:
            for node in nodes_list:
                for noder in [node.left, node.right]:
                    if noder:
                        temp_l.append(noder)

            nodes_list = temp_l[:]
            temp_l = list()
            if not nodes_list:
                break
            result += 1
        return result

# Level Order Traversal
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        if not root:
            return result

        current_level = [root]
        while True:
            next_level = [tnode for node in current_level for tnode in [node.left, node.right] if tnode]
            result += 1
            if next_level:
                current_level = next_level[:]
            else:
                break

        return result

# recursive DFS
class Solution(object):
    def maxDepth(self, root):
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

# in order (Iterative DFS)
class Solution(object):
    def maxDepth(self, root):
        result = 0
        if root:
            troot = root
        else:
            return result

        current, stack = 0, list()
        while True:
            if troot:
                stack.append((troot, current+1))
                troot = troot.left
                current += 1
            else:
                if stack:
                    troot, current = stack.pop()
                    result = max(result, current)
                    troot = troot.right
                else:
                    return result