"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes v and w as the lowest node in T 
that has both v and w as descendants (where we allow a node to be a descendant of itself)."

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# MOWN
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        list1 = self.find_node(root, p)
        list2 = self.find_node(root, q)

        return next(a for a, b in zip(list1, list2)[::-1] if a == b)  # LUP part

    def find_node(self, root, node):
        if not root:
            return list()

        elif root == node:
            return [root]

        for tnode in [root.left, root.right]:
            tresult = self.find_node(tnode, node)
            if tresult:
                return [root] + tresult

        return list()