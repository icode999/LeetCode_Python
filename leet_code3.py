"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Hide Company Tags Amazon Adobe Bloomberg Yelp
Show Tags
Show Similar Problems
"""
# MOWN solution everytime we hit a repeating char we update out start position to the char previous occurance
# Hash map
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, mapr, maxer = 0, dict(), 0
        for i in range(len(s)):
            if mapr.has_key(s[i]) and mapr[s[i]] >= start:
                start = mapr[s[i]] + 1

            mapr[s[i]] = i
            maxer = max(maxer, i-start + 1)

        return maxer