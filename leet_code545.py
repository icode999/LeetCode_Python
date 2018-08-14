"""
545. Boundary of Binary Tree

Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root.
Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

Left boundary is defined as the path from root to the left-most node.
Right boundary is defined as the path from root to the right-most node.
If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary.
Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists.
If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1
Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
Example 2
Input:
    ____1_____
   /          \
  2            3
 / \          /
4   5        6
   / \      / \
  7   8    9  10

Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].


Hide Company Tags Amazon Google
Hide Tags Tree
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

# MOWN
# Solution: left nodes + leaves + right nodes

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        elif not root.left and not root.right:
            return [root.val]

        root_val = [root.val]
        # reading left boundary
        left_boundary = list()
        troot = root.left  # Bug [1,null,2,3,4] (start from left always, handle root node value seperately)

        # exclude leaf node while getting left boundary
        while troot and (troot.left or troot.right):
            left_boundary.append(troot.val)
            troot = troot.left if troot.left else troot.right

        # reading right boundary
        right_boundary = list()
        troot = root.right

        # exclude leaf node while getting left boundary
        while troot and (troot.left or troot.right):
            right_boundary.append(troot.val)
            troot = troot.right if troot.right else troot.left

        # reading leaves

        troot = root
        stack = list()
        leaves = list()
        while True:
            if troot:
                stack.append(troot)
                troot = troot.left

            else:
                if stack:
                    troot = stack.pop()
                    if not troot.right and not troot.left:
                        leaves.append(troot.val)

                    troot = troot.right
                else:
                    break

        return root_val + left_boundary + leaves + right_boundary[::-1]

# LUP Solution
# Solution: left nodes + leaves + right nodes

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        result = [root.val]
        result_l = self.get_left(root.left)
        result_leaves_left = self.get_leaves(root.left)
        result_leaves_right = self.get_leaves(root.right)

        result_r = self.get_right(root.right)
        result += result_l
        result += result_leaves_left
        result += result_leaves_right
        result += result_r

        return result

    def get_left(self, root):
        if not root or not (root.left or root.right):
            return []

        else:
            listr = [root.val]
            if not root.left:
                temp_res = self.get_left(root.right)
            else:
                temp_res = self.get_left(root.left)

            if temp_res:
                listr += temp_res
            return listr

    def get_right(self, root):
        if not root or not (root.left or root.right):
            return []

        else:
            listr = list()
            if not root.right:
                temp_res = self.get_right(root.left)

            else:
                temp_res = self.get_right(root.right)

            if temp_res:
                listr += temp_res

            listr.append(root.val)
            return listr

    def get_leaves(self, root):
        if not root:
            return []

        listr = list()
        if root.left or root.right:
            for node in [root.left, root.right]:
                if node:
                    temp_res = self.get_leaves(node)
                    if temp_res:
                        listr += temp_res
        else:
            listr.append(root.val)
        return listr
