"""
320. Generalized Abbreviation

Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

Companies
Google
"""


# MOWN Recursive
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if not word:
            return [""]

        result = [word]
        for i in range(1, len(word) + 1):
            for j in range(len(word) - i + 1):
                tresult = self.generateAbbreviations(word[j + i + 1:])
                if len(tresult) > 0 and tresult[0]:
                    for res in tresult:
                        result.append(word[:j] + str(i) + word[j + i] + res)
                else:
                    result.append(word[:j] + str(i) + word[j + i:])

        return result