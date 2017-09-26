'''
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

Seen this question in a real interview before?   Yes  No
Difficulty:Medium
Total Accepted:112.1K
Total Submissions:427.2K
Contributor: LeetCode
Companies : Google Microsoft Uber
'''
class Solution(object):
    def spiralOrder(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not mat:
            return []
        RS, RE = 0, len(mat)
        CS, CE = 0, len(mat[0])
        result = list()
        while True:
            if CS == CE:
                  break
            for i in range(CS, CE):
                  result.append(mat[RS][i])
            RS += 1

            if RS == RE:
                  break

            for i in range(RS, RE):
                  result.append(mat[i][CE-1])
            CE -= 1

            if CS == CE:
                  break

            for i in range(CE-1, CS-1, -1):
                  result.append(mat[RE-1][i])
            RE -= 1

            if RS == RE:
                  break

            for i in range(RE-1, RS-1, -1):
                  result.append(mat[i][CS])
            CS += 1

        return result