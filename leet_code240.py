"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

Hide Company Tags Amazon Google Apple

"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for line in matrix:
            if not line or line[0] > target:
                return False
            else:
                result = self.binary_search(line, target)
                if result:
                    return result
        return False

    def binary_search(self, lista, target):
        if target > lista[-1]:
            return False
        temp = lista[:]

        while len(temp) != 0:
            pivot = len(temp)/2
            if temp[pivot] == target:
                return True

            elif temp[pivot] < target:
                temp = temp[pivot+1:]

            else:
                temp = temp[:pivot]

        return False