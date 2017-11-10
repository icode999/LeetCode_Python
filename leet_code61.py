"""
61. Rotate List

Given a list, rotate the list to the right by k places, where k is non-negative.


Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        count, thead = 0, head
        while thead:
            count += 1
            thead = thead.next
        k = k % count  # GOT TLE then changed to do modulo

        if not k:
            return head  # BUG: check if k, if not just return head

        slow = fast = head
        for _ in xrange(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        thead = slow.next
        slow.next = None
        fast.next = head

        return thead