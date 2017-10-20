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

# LUP solution  got TLE
class Solution(object):
    def combine(self, n, k):
        self.result = list()
        self.combine_l(n, k)
        return self.result

    def combine_l(self, n, k, position=0, result=list()):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if len(result) == k:
            self.result.append(result[:])
            return

        for i in range(position, n):
            result.append(i + 1)
            self.combine_l(n, k, i + 1, result)
            result.pop()

        return
