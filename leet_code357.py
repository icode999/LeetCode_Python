'''
357. Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 <= x < 100, excluding [11,22,33,44,55,66,77,88,99])

Companies
Google

'''

# MOWN
# Solution:
#add a number and increment count, backtrack. Keep a map to have all used digits

class Solution(object):
    def __init__(self):
        self.count = 1  # count 0
        self.start = True

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.Helper(n, {})
        return self.count

    def Helper(self, n, mapr):
        if n == 0:
            return

        start = 1 if self.start else 0
        self.start = False

        for j in range(start, 10):
            if mapr.has_key(j):
                continue

            self.count += 1
            mapr[j] = True
            self.Helper(n - 1, mapr)
            mapr.pop(j)

        return