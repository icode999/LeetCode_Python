"""
143. Reorder List

Given a singly linked list L: L0 - L1 - ...- Ln-1 - Ln,
reorder it to: L0 - Ln - L1 - Ln-1 - L2 - Ln-2 ... 

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.


"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# LUP solution: Split the list to half (fast, slow pointer, move fast pointer first and then slow)
# reverse the second list
# merge list1 and list2

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head:
            thead = self.split_linkedlist(head)
            head2 = self.reverse_linkedlist(thead)
            self.merge_linkedlist(head, head2)

    def merge_linkedlist(self, head1, head2):
        while head2:
            temp = head1.next
            head1.next = head2
            head2 = head2.next
            head1.next.next = temp
            head1 = temp

    def split_linkedlist(self, head):
        slow = fast = head
        while fast:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next

            else:
                break

        head = slow.next
        slow.next = None
        return head

    def reverse_linkedlist(self, head):
        current, nextt = head, None

        while current:
            temp = current.next
            current.next = nextt
            nextt = current
            head = current
            current = temp
        return head
