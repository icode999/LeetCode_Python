"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Companies 
Microsoft Amazon LinkedIn Apple 
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = temp = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next

            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next

        if not l2:
            temp.next = l1

        if not l1:
            temp.next = l2

        return result.next