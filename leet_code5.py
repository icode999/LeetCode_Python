"""
5. Longest Palindromic Substring


Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
Hide Company Tags Amazon Microsoft Bloomberg
Hide Tags String
Hide Similar Problems (H) Shortest Palindrome (E) Palindrome Permutation (H) Palindrome Pairs (M) Longest Palindromic Subsequence


"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        def palin_expand(i, j):
            ti, tj = False, False
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    ti, tj = i, j
                    i, j = i-1, j+1
                else:
                    break
            return [ti, tj+1] if tj else False

        palin = [0, 1]
        for i in range(len(s)):
            for t1, t2 in [[i-1, i+1], [i, i+1]]:
                result = palin_expand(t1, t2)
                if result:
                    palin = palin[:] if palin[1]-palin[0] > result[1]-result[0] else result[:]
        return s[palin[0]:palin[1]]