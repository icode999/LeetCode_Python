"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        mapr1, mapr2 = dict(), dict()
        for i in range(len(s)):
            if (mapr1.has_key(s[i]) and mapr1[s[i]] != t[i]) or (mapr2.has_key(t[i]) and mapr2[t[i]] != s[i]):
                return False

            mapr1[s[i]] = t[i]
            mapr2[t[i]] = s[i]

        return True