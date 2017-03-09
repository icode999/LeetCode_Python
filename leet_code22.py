"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
Hide Company Tags Google Uber Zenefits
Show Tags
Hide Similar Problems
"""

# LUP
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = list()
        def generate(open, close, string):
            if len(string) == 2*n:
                result.append(string)
                return

            if open < n:
                generate(open+1, close, string+'(')

            if close < open:
                generate(open, close+1, string+')')

        generate(0, 0, '')
        return result
