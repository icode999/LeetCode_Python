"""
763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.

Companies
Amazon 5
"""
from collections import defaultdict
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = list()
        mapr = defaultdict(list)
        for idx, char in enumerate(S):
            mapr[char].append(idx)

        start = 0
        while start < len(S):
            end = mapr[S[start]][-1]
            current = set(S[start])
            tstart = start
            start += 1

            while start <= end:
                if S[start] not in current:
                    end = max(mapr[S[start]][-1], end)
                    current.add(S[start])

                start += 1

            result.append(start - tstart)

        return result
