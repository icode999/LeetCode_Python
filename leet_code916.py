"""
916. Word Subsets

We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a.

Return a list of all universal words in A.  You can return the words in any order.



Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]

Companies
Google

"""
# MOWN after TLE
# For array B we have to get counter for the entire array once instead of O(AB)
from collections import Counter, defaultdict


class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        CounterA = [Counter(a) for a in A]
        CounterB = defaultdict(int)

        for b in B:
            for char, count in Counter(b).iteritems():
                CounterB[char] = max(CounterB[char], count)

        result = list()
        for i in range(len(A)):
            for char, count in CounterB.iteritems():
                if char not in CounterA[i] or CounterA[i][char] < count:
                    break

            else:
                result.append(A[i])

        return result