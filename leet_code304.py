"""
304. Range Sum Query 2D - Immutable

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
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 <= row2 and col1 <= col2.


Hide Tags Dynamic Programming
Show Similar Problems

"""

class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sum_matrix = [[0]*len(matrix[0]) for j in range(len(matrix))]
        for i in range(len(matrix)):
            summ = 0
            for j in range(len(matrix[0])):
                summ += matrix[i][j]
                self.sum_matrix[i][j] = summ

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
# param_1 = obj.sumRegion(row1,col1,row2,col2)