# -*- coding: utf-8 -*-
"""
428. Serialize and Deserialize N-ary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree

 



 

as [1 [3[5 6] 2 4]]. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Note:

N is in the range of [1, 1000]
Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
# LUP
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:
    def serialize(self, root):	
        serial = list()
        def pre_order(node):
            if not node:
                return 
            
            serial.append(str(node.val))
            for child in node.children:
                pre_order(child)
            
            serial.append("#")
        
        pre_order(root)  
        return ",".join(serial)
            
    def deserialize(self, data):
        if not data:
            return None
        
        data = data.split(",")
        node = Node(int(data.pop(0)), [])
        
        def pre_order(node):
            if not data:
                return 
            
            while data[0] != "#":
                tnode = Node(int(data.pop(0)), [])
                node.children.append(tnode)
                pre_order(tnode)
            
            data.pop(0)
        
        pre_order(node)
        return node
