"""
896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true


Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000

Companies
"""
# MOWN 2 pass
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        def is_increasing(listr):
            current = listr[0]
            for i in range(1, len(listr)):
                if current >= listr[i]:
                    current = listr[i]
                else:
                    return False
            return True

        return A and (is_increasing(A) or is_increasing(A[::-1]))

# LUP 2 pass
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return A and (all(A[i] <= A[i+1] for i in range(len(A)-1)) or all(A[i] <= A[i-1] for i in range(len(A)-1, 0, -1)))


# LUP 1 pass
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        cmpp = 0
        for i in range(len(A) - 1):
            tcmp = cmp(A[i], A[i + 1])
            if tcmp:
                if tcmp != cmpp != 0:
                    return False
                cmpp = tcmp

        return True
