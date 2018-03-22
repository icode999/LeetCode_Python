"""
161. One Edit Distance

Given two strings S and T, determine if they are both one edit distance apart.

Companies 
Facebook Uber Twitter Snapchat

"""
# LUP
# Three cases
'''
 * 1) Replace 1 char:
 	  s: a B c
 	  t: a D c
 * 2) Delete 1 char from s: 
	  s: a D  b c
	  t: a    b c
 * 3) Delete 1 char from t
	  s: a   b c
	  t: a D b c

'''
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t or abs(len(s) - len(t)) > 1:
            return False

        return self.Helper(s, t) if len(s) <= len(t) else self.Helper(t, s)

    def Helper(self, s, t, c=0):
        for i in range(len(s)):
            if s[i] != t[i]:
                return s[i + 1:] == t[i + 1:] or s[i:] == t[i + 1:]

        return True