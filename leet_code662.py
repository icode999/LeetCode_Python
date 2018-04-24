"""
662. Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:
Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:
Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:
Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.

Companies
Poynt

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# MOWN Solution
# BFS, ignore all Null node at the start and end of each level and get max length
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        current = [root]
        result = 0

        while current:
            next_level = list()
            none_counter = 0

            for node in current:
                if not node:
                    none_counter += 2

                else:
                    for tnode in [node.left, node.right]:
                        if tnode:
                            if next_level:  # BUG : [1,1,1,1,1,1,1,null,null,null,1,null,null,null,null,2,2,2,2,2,2,2,null,2,null,null,2,null,2]
                                # strip all the none from starting and ending of the next_level
                                next_level += [None] * none_counter

                            next_level += [tnode]
                            none_counter = 0
                        else:
                            none_counter += 1

            result = max(result, len(current))
            current = next_level

        return result


# LUP Solution
# BFS, give each a node a pos, its left child will have pos: root_pos*2, right child will have pos: root_pos*2+1
# (root will have 0, left child pos is 0 and right child pos is 1)
# everytime we got to next level we have to save the pos of left, so no.of nodes will be right_pos - left_pos + 1, we take max

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [(root, 0, 0)]
        current_depth, left, result = 0, 0, 0

        for node, depth, pos in stack:
            if node:
                stack.append((node.left, depth + 1, pos * 2))
                stack.append((node.right, depth + 1, pos * 2 + 1))

                if depth != current_depth:
                    current_depth = depth
                    left = pos

                result = max(result, pos - left + 1)

        return result
