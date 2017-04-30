"""
17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

Hide Company Tags Amazon Dropbox Google Uber Facebook
Hide Tags Backtracking String
Hide Similar Problems (M) Generate Parentheses (M) Combination Sum (E) Binary Watch
"""

# MOWN solution backtracking
class Solution(object):
    def __init__(self):
        self.mapr = {'1': ['*'], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return self.getcombinations(list(digits))

    def getcombinations(self, listr):
        """
        listr = ['1', '2', '3']
        """
        result = list()
        if len(listr) == 1:
            return self.mapr[listr[0]]

        elif not listr:
            return []

        else:
            tresult = self.getcombinations(listr[1:])
            for char in self.mapr[listr[0]]:
                for temp in tresult:
                    result.append(char+temp)

        return result
