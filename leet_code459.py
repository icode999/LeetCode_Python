"""
459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

Hide Company Tags Amazon Google
Hide Tags String
Hide Similar Problems (E) Implement strStr()

"""

# MOWN solution (1150 msec)
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tstr = ''
        for i in range(len(s)/2 + 1):
            tstr += s[i]
            count = len(s)/len(tstr)
            if count != 1 and tstr*(count) == s:
                return True
        return False


# LUP solution
#First char of input string is first char of repeated substring
#Last char of input string is last char of repeated substring
#Let S1 = S + S (where S in input string)
#Remove 1 and last char of S1. Let this be S2
#If S exists in S2 then return true else false

class Solution(object):
    def repeatedSubstringPattern(self, s):
        return True if s in (s*2)[1:-1] else False
