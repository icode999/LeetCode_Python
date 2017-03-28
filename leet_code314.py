"""
314. Binary Tree Vertical Order Traversal

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
return its vertical order traversal as:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
Hide Company Tags Google Snapchat Facebook
Hide Tags Hash Table
Hide Similar Problems
"""

#Solution: Do in order iterative
# Doing in order which will give wrong answer interms of "If two nodes are in the same row and column, the order should be from left to right.", but will give correct answer if you dont have that.
from collections import defaultdict
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        stack = list()
        mapr = defaultdict(list)

        troot, counter = root, 0
        while True:
            if troot:
                stack.append((counter, troot))
                troot = troot.left
                counter -= 1

            else:
                if stack:
                    counter, troot = stack.pop()
                    mapr[counter].append(troot.val)
                    troot = troot.right
                    counter += 1
                else:
                    break

        keyss = mapr.keys()
        keyss.sort()
        result = list()
        for key in keyss:
            result.append(mapr[key])
        return result
