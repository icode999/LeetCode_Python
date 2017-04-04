"""
159. Longest Substring with At Most Two Distinct Characters

Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = "eceba"

T is "ece" which its length is 3.

Hide Company Tags Google
Show Tags
Show Similar Problems
"""

# Solution: o(n) run time and o(1) space, just save two distinct chars latest occurance. When third
# distinct char comes update the minimum char

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        start, mapr, maxer = 0, [[s[0], 0]], 1
        for i in range(1, len(s)):
            if len(mapr) == 1:
                if mapr[0][0] == s[i]:
                    mapr[0][1] = i
                else:
                    mapr.append([s[i], i])


            else:
                for j in range(2):
                    if mapr[j][0] == s[i]:
                        mapr[j][1] = i
                        break
                else:
                    if mapr[0][1] < mapr[1][1]:
                        temp = 0
                    else:
                        temp = 1

                    start = mapr[temp][1] + 1
                    mapr[temp] = [s[i], i]

            maxer = max(maxer, i-start+1)

        return maxer
