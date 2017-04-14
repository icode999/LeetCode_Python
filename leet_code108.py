"""
108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Hide Company Tags Airbnb
Hide Tags Tree Depth-first Search
Hide Similar Problems (M) Convert Sorted List to Binary Search Tree
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# MOWN
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        elif len(nums) == 1:
            return TreeNode(nums[0])

        else:
            pivot = (len(nums)-1)/2
            root = TreeNode(nums[pivot])
            root.left = self.sortedArrayToBST(nums[:pivot])
            root.right = self.sortedArrayToBST(nums[pivot+1:])

            return root