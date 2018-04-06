"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""

# MOWN
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.Helper(range(1, n + 1), k)

    def Helper(self, listr, n):
        if n > len(listr) or n == 0:
            return []

        if n == 1:
            return [[i] for i in listr]

        result = list()
        for i in range(len(listr)):
            tresult = self.Helper(listr[i + 1:], n - 1)
            if tresult:
                result += [[listr[i]] + temp for temp in tresult]

        return result
