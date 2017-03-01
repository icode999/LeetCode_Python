"""
266. Palindrome Permutation

Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

Hint:

Consider the palindromes of odd vs even length. What difference do you notice?
Count the frequency of each character.
If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?


Hide Company Tags Google Uber Bloomberg
Show Tags
Show Similar Problems
"""
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapr = dict()
        for char in s:
            if mapr.has_key(char):
                mapr[char] += 1
            else:
                mapr[char] = 1
        count = 0
        for char in mapr.keys():
            if mapr[char] % 2 != 0:
                count += 1
                if count > 1:
                    return False
        return True