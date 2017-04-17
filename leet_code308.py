"""
308. Range Sum Query 2D - Mutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 <= row2 and col1 <= col2.


Hide Company Tags Google
Hide Tags Binary Indexed Tree Segment Tree
Show Similar Problems

"""

# MOWN Solution
# we build a sum_matrix, at each i, j it holds for i th column sum(0, j)
# result will be from row1 to row2 we get sum[row1][col2] - sum[row1][col1]
# O(mn) time and o(mn) space
class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sum_matrix = [[0]*len(matrix[0]) for j in range(len(matrix))]
        self.matrix = matrix
        for i in range(len(matrix)):
            summ = 0
            for j in range(len(matrix[0])):
                summ += matrix[i][j]
                self.sum_matrix[i][j] = summ

        #print self.sum_matrix

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        for i in range(col, len(self.sum_matrix[0])):
            self.sum_matrix[row][i] += diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        result = 0
        for i in range(row1, row2+1):
            if col1 != 0:
                result += self.sum_matrix[i][col2] - self.sum_matrix[i][col1-1]
            else:
                result += self.sum_matrix[i][col2]

        return result



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)