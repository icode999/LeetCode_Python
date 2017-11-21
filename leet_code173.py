"""
173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

"""
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.inorder_iter = self.binary_tree_iterator(root)
        self.next_element = None

    def binary_tree_iterator(self, root):
        stack, current = list(), root
        while True:
            if current:
                stack.append(current)
                current = current.left

            else:
                if stack:
                    current = stack.pop()
                    yield current.val
                    current = current.right

                else:
                    break

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.next_element != None:
            return True

        try:
            self.next_element = self.inorder_iter.next()
            return True
        except Exception:
            return False

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            result = self.next_element
            self.next_element = None
            return result
        else:
            return None






# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())