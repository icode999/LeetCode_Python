"""
344. Reverse String

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

Hide Tags Two Pointers String
Show Similar Problems

"""
# regular method
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start, end = 0, len(s)-1
        while start < end:
            s[end], s[start] = s[start], s[end]
            start += 1
            end -= 1

        return ''.join(s)


# Pythonic method
class Solution(object):
    def reverseString(self, s):
        return s[::-1]