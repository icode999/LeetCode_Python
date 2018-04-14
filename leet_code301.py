"""
301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
Credits:
Special thanks to @hpplayer for adding this problem and creating all test cases.

Hide Company Tags Facebook
Show Tags
Show Similar Problems

"""

# BFS
# check for valid in all possibilities
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def is_valid(string):
            count = 0
            for char in string:
                count += (char == "(") - (char == ")")
                if count < 0:
                    return False
            return count == 0

        level = {s}
        while True:
            result = filter(is_valid, level)
            if result:
                return result

            level = {word[:i] + word[i + 1:] for word in level for i in range(len(word)) if word[i] in ["(", ")"]}


# LUP Solution
# https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = list()
        self.remove(s, 0, 0, ["(", ")"])
        return self.result

    def remove(self, s, li, lj, par):
        counter = 0
        for i in range(li, len(s)):
            counter += (s[i] == par[0]) - (s[i] == par[1])

            if counter >= 0:
                continue

            for j in range(lj, i + 1):
                if s[j] == par[1] and (j == lj or s[j - 1] != par[1]): #  s[j-1] != pra[1] we check this so that we dont generate repeated combinations
                    self.remove(s[:j] + s[j + 1:], i, j, par)

            return

        reverse = s[::-1]
        if par[0] == "(":
            self.remove(reverse, 0, 0, [")", "("])
        else:
            self.result.append(reverse)
