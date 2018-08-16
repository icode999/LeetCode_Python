"""
844. Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".


Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Companies
Google

"""
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def nextr(string):
            skip = 0
            for char in reversed(string):
                if char == "#":
                    skip += 1

                elif skip:
                    skip -= 1

                else:
                    yield char

        s_next, t_next = nextr(S), nextr(T)
        while True:
            x, y = next(s_next, None), next(t_next, None)
            if x == y:
                if x == None and y == None:
                    break
            else:
                return False

        return True

# MOWN using stack
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def get_string(string):
            stack = list()
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()

                else:
                    stack.append(char)

            return stack

        return get_string(S) == get_string(T)