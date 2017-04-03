"""
340. Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = "eceba" and k = 2,

T is "ece" which its length is 3.

Hide Company Tags Google
Show Tags
Show Similar Problems
"""

# MOWN solution
# maintain hash map, update maxer for every char and len of mapr is less than k
# if len(mapr) > k we should decrement mapr[char[start]] and increment start (remove entry from mapr if count is 0)

from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mapr = defaultdict(int)
        start, maxer = 0, 0
        for i in range(len(s)):
            mapr[s[i]] += 1
            if len(mapr) <= k:
                maxer = max(maxer, i-start+1)
            else:
                mapr[s[start]] -= 1
                if mapr[s[start]] == 0:
                    mapr.pop(s[start])
                start += 1
        return maxer
