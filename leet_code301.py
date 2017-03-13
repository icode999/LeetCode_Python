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

"""
Solution:

BFS, with the input string s, we generate all possible states by removing one ( or ), check if they are valid, if found valid ones on the current level, put them to the final result list and we are done, otherwise, add them to a queue and carry on to the next level.

However, it does it implicitly. For a string of parentheses to be valid, its number of parentheses should be even. And at any time, strings in queue will only differ in length of 1 (this is the implicit control). When we find "()()" to be valid, both "()" and "" have not been added to queue yet and all the shorter strings are of length of 3, which must be invalid.

Once we hit found, we will not add any other levels to our queue, Also since all the valid parentheses will have even number of parentheses, whatever the added next level parentheses will be False anyways

"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False

            return count == 0

        result = list()
        visited = dict()
        queue = list()

        if is_valid(s):
            return [s]

        else:
            queue.append(s)
            visited[s] = True

        found = False
        while queue:
            tmp_str = queue.pop(0)
            if is_valid(tmp_str):
                result.append(tmp_str)
                found = True

            if found:
                continue

            for i in range(len(tmp_str)):
                if tmp_str[i] not in ['(', ')']:
                    continue

                temp = tmp_str[:i] + tmp_str[i+1:]
                if not visited.has_key(temp):
                    queue.append(temp)
                    visited[temp] = True

        return result

