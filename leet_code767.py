"""
767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].

Companies
Google
"""
# MOWN using priority queue
from collections import Counter
from Queue import PriorityQueue
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = Counter(S)
        pq = PriorityQueue()
        for letter, count in counter.iteritems():
            pq.put([count * -1, letter])

        result = ""
        while not pq.empty():
            count, char = pq.get()
            result += char
            count += 1
            if count != 0:
                if not pq.empty():
                    tcount, tchar = pq.get()
                    result += tchar
                    tcount += 1
                    pq.put([count, char])
                    if tcount != 0:
                        pq.put([tcount, tchar])
                else:
                    result = ""
                    break

        return result
