"""
297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

Credits:
Special thanks to @Louis1992 for adding this problem and creating all test cases.

Hide Company Tags LinkedIn Google Uber Facebook Amazon Microsoft Yahoo Bloomberg
Show Tags
Show Similar Problems

"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

#Solution : BFS or level order ([1,2,3,null,null,4] --->  "1,2,3,#,#,4,#,#,#")
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None

        result = str(root.val)
        level_nodes = [root.left, root.right]

        while True:
            next_level_nodes = list()
            while level_nodes:
                troot = level_nodes.pop(0)
                result += ','
                if troot:
                    result += str(troot.val)
                    for node in [troot.left, troot.right]:
                        next_level_nodes.append(node)
                else:
                    result += '#'

            if next_level_nodes:
                level_nodes = next_level_nodes[:]
            else:
                print result
                return result


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes_list = data.split(',')
        root = TreeNode(int(nodes_list.pop(0)))

        current_level_nodes = [root]


        while True:
            next_level_nodes = list()
            while current_level_nodes:
                node = current_level_nodes.pop(0)
                lt = nodes_list.pop(0)
                rt = nodes_list.pop(0)

                if lt != '#':
                    node.left = TreeNode(int(lt))
                    next_level_nodes.append(node.left)
                if rt != '#':
                    node.right = TreeNode(int(rt))
                    next_level_nodes.append(node.right)

            if not next_level_nodes:
                return root

            else:
                current_level_nodes = next_level_nodes[:]

#Solution : DFS/preorder ([1, 2, 3, 4, 5, 6, 7] --->  1,2,4,n,n,5,n,n,3,6,n,n,7,n,n)
# serializing is trivial , just pre order iterative, however de-serialize is tricky, you have to maintain flags to insert left or right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None

        result = ''
        stack = list()
        troot = root
        while True:
            if troot:
                stack.append(troot)
                result += str(troot.val) + ','
                troot = troot.left
            else:
                result += 'n,'
                if stack:
                    troot = stack.pop()
                    troot = troot.right
                else:
                    result = result.rstrip(',')
                    print result
                    return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data_list = data.split(',')
        root = TreeNode(str(data_list.pop(0)))

        stack, troot, left = list(), root, True
        for val in data_list:
            if val != 'n':
                if left:
                    stack.append(troot)
                    troot.left = TreeNode(str(val))
                    troot = troot.left
                else:
                    troot.right = TreeNode(str(val))
                    troot = troot.right
                left = True

            else:
                if not left:
                    if stack:
                        troot = stack.pop()
                    else:
                        return root
                else:
                    left = False

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
