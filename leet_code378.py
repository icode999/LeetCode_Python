"""
378. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 <= k <= n2.
"""
# MOWN
# Use priority queue
# since we need to get kth least we keep our queue size K and remove an element from queue if > current element
# since we are using priority queue, we need to multiply wach number by -1 so when we do pq.get we get the highest number from Que
from Queue import PriorityQueue


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        pq = PriorityQueue(k)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if pq.full():
                    num = pq.get()
                    if num < matrix[i][j] * -1:
                        pq.put(matrix[i][j] * -1)
                    else:
                        pq.put(num)
                else:
                    pq.put(matrix[i][j] * -1)

        return pq.get() * -1