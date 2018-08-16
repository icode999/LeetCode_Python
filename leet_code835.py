"""
835. Image Overlap

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes:

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1

Companies
Google
"""
# LUP
# for each 1 in A get the distance to each 1 in B
# now get the distance that have max 1's (which gives u max overlap of 1s)

from collections import defaultdict
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        A1 = [(i, j) for i in range(len(A)) for j in range(len(A[0])) if A[i][j] == 1]
        B1 = [(i, j) for i in range(len(B)) for j in range(len(B[0])) if B[i][j] == 1]

        mapr = defaultdict(int)
        result = 0

        for a1 in A1:
            for b1 in B1:
                temp = (b1[0] - a1[0], b1[1] - a1[1])
                mapr[temp] += 1
                result = max(result, mapr[temp])

        return result
