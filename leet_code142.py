# -*- coding: utf-8 -*-
"""
142.
Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

Companies   
Microsoft 3Bloomberg 3Adobe 3Google 2Tencent 2

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        def get_intersection():
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            else:
                return None
        
        end = get_intersection()
        if not end:
            return None
        
        start = head
        
        while start != end:
            start = start.next
            end = end.next
        
        return start 
