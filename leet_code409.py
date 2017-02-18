"""
409. Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Hide Company Tags Google
Show Tags
Show Similar Problems

"""

# My solution
class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapr = dict()
        for char in s:
            if mapr.has_key(char):
                mapr[char] += 1
            else:
                mapr[char] = 1

        result = 0
        odd = False
        for key, value in mapr.iteritems():
            if value % 2 == 0:
                result += value   # add value since it counts the occurances of key
            else:
                result += value-1  # Did a mistake here, need to add (odd occurances)-1 as well to result For example "ccc"
                odd = True

        return result+1 if odd else result

# looked up solution
import collections
class Solution2(object):
    def longestPalindrome(self, s):
        mapr = collections.Counter(s)
        #odds = sum(i % 2 for i in mapr.values())
        odds = sum(i & 1 for i in mapr.values())
        return len(s) - odds + bool(odds)