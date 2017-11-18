""" 
647. Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
The input string length won't exceed 1000.

"""
# LUP Solution
# expand from all centers that are available in the entire string (2N-1 centers)
# left will be moved every two times and right will be moved every two times
# hence left = center/2 and right = center/2 + center%2

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        result = 0
        for center in range(2 * len(s) - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    result += 1
                    left -= 1
                    right += 1
                else:
                    break

        return result