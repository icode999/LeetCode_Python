'''
357. Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 <= x < 100, excluding [11,22,33,44,55,66,77,88,99])

'''

# MOWN

from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mapr = defaultdict(int)
        for num in nums:
            mapr[num] += 1

        keys = mapr.keys()
        keys.sort(key=lambda x: (-mapr[x], x))
        return keys[:k]