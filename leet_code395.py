"""
395. Longest Substring with At Least K Repeating Characters

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Companies
Baidu
"""
# LUP
# get the minimum repeated char and check if its frequency is less than K, if so we split s based on that minor and
# make a recursive call
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        minor = min(set(s), key=s.count)
        if s.count(minor) >= k:
            return len(s)

        return max(self.longestSubstring(sub_string, k) for sub_string in s.split(minor))
