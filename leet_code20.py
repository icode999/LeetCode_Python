"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Hide Company Tags Google Airbnb Facebook Twitter Zenefits Amazon Microsoft Bloomberg
Show Tags
Show Similar Problems

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapr = {'(':')', '{':'}', '[':']'}

        stack = list()
        for char in s:
            if mapr.has_key(char):
                stack.append(mapr[char])
            else:
                if stack and stack.pop() == char:
                    continue
                else:
                    return False
        return False if stack else True

