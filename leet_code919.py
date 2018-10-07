"""
919. Complete Binary Tree Inserter

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.


Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]


Note:

The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.

"""
# MOWN solution
# keep previous level and current level
class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.previous = [root]
        self.current = [node for node in [root.left, root.right] if node]
        self.level = 1

        while len(self.current) == pow(2, self.level):
            next_l = list()
            for node in self.current:
                for tnode in [node.left, node.right]:
                    if not tnode:
                        break
                    next_l.append(tnode)

            self.previous = self.current
            self.current = next_l
            self.level += 1

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        position = len(self.current) / 2
        right = len(self.current) % 2
        self.current.append(node)
        troot = self.previous[position]

        if right:
            troot.right = node
        else:
            troot.left = node

        if len(self.current) == pow(2, self.level):
            self.previous = self.current[:]
            self.current = list()
            self.level += 1

        return troot.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root