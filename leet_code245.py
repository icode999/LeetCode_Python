"""
245. Shortest Word Distance III

This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "makes", word2 = "coding", return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
"""


# MOWN
# if word1 == word2 and word == word1, we take abs diff between index1 and i
# make sure index1 gets the updated value
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1 = index2 = result = len(words)
        for i in range(len(words)):
            if words[i] == word1 and word1 == word2:
                temp = index1
                index1 = i
                result = min(result, abs(index1 - temp))

            elif words[i] == word1:
                index1 = i
                result = min(result, abs(index1 - index2))

            elif words[i] == word2:
                index2 = i
                result = min(result, abs(index1 - index2))

        return result