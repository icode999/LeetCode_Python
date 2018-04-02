"""
750. Number Of Corner Rectangles

Given a grid where each entry is only 0 or 1, find the number of corner rectangles.

A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.



Example 1:

Input: grid =
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].


Example 2:

Input: grid =
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.


Example 3:

Input: grid =
[[1, 1, 1, 1]]
Output: 0
Explanation: Rectangles must have four distinct corners.


Note:

The number of rows and columns of grid will each be in the range [1, 200].
Each grid[i][j] will be either 0 or 1.
The number of 1s in the grid will be at most 6000.

Companies
Facebook
"""

# MOWN solution got TLE
# Check each element one by one
class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    continue

                for tc in range(col + 1, len(grid[0])):
                    if grid[row][tc] == 0:
                        continue

                    for tr in range(row + 1, len(grid)):
                        result += grid[tr][tc] and grid[tr][col]
        return result

"""
If you look at the inner loops of indices "j, q" more carefully, what they do is essentially counting the number of pairs (j, q) 
such that grid[i][j] == 1 && grid[p][j] == 1 as well as grid[i][q] == 1 && grid[p][q] == 1, assuming j != q
It turns out this can be done by looping through the rows only once, as explained below.

Imagine we have a 1D array nums of numbers 0 and 1, and we d like to count the number of pairs (j, q) 
such that nums[j] == 1 as well as nums[q] == 1, assuming j != q. Of course, we can use two nested loops to find the answer. 
Now what if I tell you that the number of 1s in the array is c? Can you figure out the answer immediately? 
I bet you can its given by (c * (c-1))/2, which is equivalent to choosing two 1s from c 1s. 
Okay, do we need two nested loops to find the number of 1s in the array? Surely we dont a linear scan would do the job perfectly. 
So in short, we can figure out the number of pairs (j, q) using a linear scan.

"""

# LUP solution1 got TLE
# Idea is to iterate rows instead columns
# for each two row we get count of No.of places we have both rows i.e grid[row1][j] and grid[row2][j]
# once we get that count, all we have to do is select 2 items out of it nc2 --> n!/2!*(n-1)! => n(n-1)/2

class Solution1(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for row in range(len(grid)):
            for trow in range(row + 1, len(grid)):
                count = 0
                for tcol in range(len(grid[0])):
                    count += grid[row][tcol] == 1 and grid[trow][tcol] == 1

                result += count * (count - 1) >> 1

        return result


# MOWN got TLE

class Solution2(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for row in range(len(grid)):
            for trow in range(row + 1, len(grid)):
                # do AND of two rows and then count No.of 1s
                temp = int(''.join([str(item) for item in grid[row]]), 2) & int(
                    ''.join([str(item) for item in grid[trow]]), 2)
                count = 0

                # count No.of 1s
                while temp:
                    temp &= temp - 1
                    count += 1

                result += count * (count - 1) >> 1

        return result


# MOWN DP solution
# for each row (row1) join all elements and convert it int and save in dp
# for each second row (row2), do AND of row1 and row2 and count No.of 1s which will give No.of pairs of 1s in both rows

'''
# example:

1 1 1 1
0 1 1 0
---------
0 1 1 0  (AND)  --- it have two 1s, i.e there will be 1 corner rectangle (nc2-->  2c2 --> 1)
---------
'''

# ACCEPTED beat 85%
class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        self.dp = {}
        for row in range(len(grid)):
            if row not in self.dp:
                self.dp[row] = int(''.join([str(item) for item in grid[row]]), 2)

            for trow in range(row + 1, len(grid)):
                if trow not in self.dp:
                    self.dp[trow] = int(''.join([str(item) for item in grid[trow]]), 2)

                    # do AND of two rows and then count No.of 1s
                temp = self.dp[row] & self.dp[trow]
                count = 0

                # count No.of 1s
                while temp:
                    temp &= temp - 1
                    count += 1

                result += count * (count - 1) >> 1

        return result
