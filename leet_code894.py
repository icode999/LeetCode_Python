# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# LUP Solution
# Thus, for N >= 3, we can formulate the recursion:
# FBT(N) =FBT(N)= [All trees with left child from \text{FBT}(x)FBT(x)
# and right child from FBT(N-1-x) FBT(N-1-x), for all x]

# Companies
# Google
class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []

        elif N == 1:
            return [TreeNode(0)]

        else:
            result = list()
            for x in range(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)

            return result