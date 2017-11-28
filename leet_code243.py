"""
243. Shortest Word Distance

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

Companies 
LinkedIn 
"""

# Solution: iterate through list of words and calculate distance everytime u hit either word1 or word2
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1 = index2 = result = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                index1 = i
                result = min(result, abs(index1 - index2))

            elif words[i] == word2:
                index2 = i
                result = min(result, abs(index1 - index2))

        return result