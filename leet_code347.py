"""
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Companies
Yelp Pocket Gems

"""

# MOWN + LUP
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        mapr = defaultdict(int)
        for word in words:
            mapr[word] += 1
        keys = mapr.keys()

        keys.sort(key=lambda x: (-mapr[x], x))
        return keys[:k]