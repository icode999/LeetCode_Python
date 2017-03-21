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
class Solution1(object):
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

# instead of copying we just used indexes in binary search
class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binary_search(lista):
            if target > lista[-1]:
                return False
            start = 0
            end = len(lista)

            while start != end:
                pivot = (start + end)/2
                if lista[pivot] == target:
                    return True

                elif lista[pivot] < target:
                    start = pivot+1

                else:
                    end = pivot

            return False

        for line in matrix:
            if not line or line[0] > target:
                return False
            else:
                result = binary_search(line)
                if result:
                    return result
        return False

# LUP idea
#The idea is to search from the top-right element and then reduce the range for further searching by comparisons between target and the current element.

# Suppose we want to search for 12. We first initialize r = 0 and c = 4. We compare 12 with matrix[r][c] = matrix[0][4] = 15 and 12 < 15, so 12 cannot appear in the column of 15 since all elements below 15 are not less than 15. Thus, we decrease c by 1 and reduce the search range by a column. Now we compare 12 with matrix[r][c] = matrix[0][3] = 11 and 12 > 11, so 12 cannot appear in the row of 11 since all elements left to 11 are not greater than 11. Thus, we increase r by 1 and reduce the search range by a row. Then we reach matrix[1][3] = 12 = target and we are done (return true). If we have moved beyond the matrix and have not found the target, return false.

class Solution3(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        row, col = 0, len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1

        return False