"""
369. Plus One Linked List

Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example:
Input:
1->2->3

Output:
1->2->4
Hide Company Tags Google
Hide Tags Linked List
Show Similar Problems

"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        num, thead = 0, head
        while thead:
            num = num*10 + thead.val
            thead = thead.next
        num += 1
        num, thead, counter = str(num), head, 0
        previous = None
        while thead:
            thead.val = int(num[counter])
            counter += 1
            previous = thead
            thead = thead.next

        if counter == len(num)-1:
            node = ListNode(int(num[counter]))
            previous.next = node

        return head