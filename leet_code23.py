"""
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

Companies
Amazon 22 Facebook 11 Google 8 Microsoft 5 Apple 4 Alibaba 4 Tencent 4 Uber 3 Bloomberg 3 Paypal 2 Dropbox 2 Oracle 2

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = PriorityQueue()
        for listr in lists:
            if listr:
                pq.put([listr.val, listr])

        current = root = None
        while not pq.empty():
            _, troot = pq.get()
            if not root:
                root = troot
                current = root

            else:
                current.next = troot
                current = current.next

            if troot.next:
                pq.put([troot.next.val, troot.next])

            current.next = None

        return root