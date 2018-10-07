"""
915.Partition Array into Disjoint Intervals

Given an array A, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.



Example 1:

Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]


Note:

2 <= A.length <= 30000
0 <= A[i] <= 10^6
It is guaranteed there is at least one way to partition A as described.

"""
# MOWN solution
# Iterate through the array once
# Keep current min and current max, as soon as we hit something smaller than current min
# our max becomes current min and result is None
# everytime we hit a new maxx, if result is None make result current index
class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return -1

        minn = maxx = A[0]
        result_idx = None

        for i in range(1, len(A)):
            if A[i] < minn:
                minn = maxx
                result_idx = None

            if A[i] >= maxx:
                maxx = A[i]
                if not result_idx:
                    result_idx = i

        return result_idx