"""
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Companies
Amazon 22Microsoft 19Bloomberg 11Google 6Facebook 5Alibaba 3Adobe 3Mathworks 2

"""
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# MOWN using map
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        node_map = dict()
        thead = head

        rhead = RandomListNode(head.label) if head else None
        rthead = rhead

        node_map[thead] = rhead

        while thead:
            if thead.random:
                if thead.random in node_map:
                    rthead.random = node_map[thead.random]

                else:
                    rand_node = RandomListNode(thead.random.label)
                    node_map[thead.random] = rand_node
                    rthead.random = rand_node

            if thead.next:
                if thead.next in node_map:
                    rthead.next = node_map[thead.next]

                else:
                    next_node = RandomListNode(thead.next.label)
                    node_map[thead.next] = next_node
                    rthead.next = next_node

            thead = thead.next
            rthead = rthead.next

        return rhead