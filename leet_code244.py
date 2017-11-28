"""
244. Shortest Word Distance II

This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

Companies 
LinkedIn 
"""
from collections import defaultdict

class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.mapr = defaultdict(list)
        for i in range(len(words)):
            self.mapr[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        result = abs(self.mapr[word1][0] - self.mapr[word2][0])
        '''
        for w1 in self.mapr[word1]:
            for w2 in self.mapr[word2]:
                result = min(result, abs(w1-w2))
        '''
        # LUP
        # finding the difference
        i, j, w1, w2 = 0, 0, self.mapr[word1], self.mapr[word2]
        while i < len(w1) and j < len(w2):
            result = min(result, abs(w1[i] - w2[j]))
            if w1[i] < w2[j]:
                i += 1
            else:
                j += 1
        return result
