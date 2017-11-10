"""
328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

"""


# MOWN solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        odd, even, te = head, head.next, head.next
        thead = head.next.next

        while thead:
            odd.next = thead
            odd = odd.next

            if thead.next:
                even.next = thead.next
                even = even.next
            else:
                even.next = None  # bug in case of odd number linkedlist there will be loop if we dont set even.next = None
                break

            thead = thead.next.next

        odd.next = te
        thead = head
        while thead:
            print thead.val
            thead = thead.next

        return head