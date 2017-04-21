"""
116. Populating Next Right Pointers in Each Node

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

Hide Company Tags Microsoft
Hide Tags Tree Depth-first Search
Hide Similar Problems (M) Populating Next Right Pointers in Each Node II (M) Binary Tree Right Side View
"""

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        current_level = [root]

        while True:
            next_level = list()
            nextr = None
            for node in current_level:
                for tnode in [node.left, node.right]:
                    if tnode:
                        if nextr:
                            nextr.next = tnode
                            nextr = tnode
                        else:
                            nextr = tnode

                        next_level.append(tnode)
            if next_level:
                current_level = next_level[:]
            else:
                break
