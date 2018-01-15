"""
720. Longest Word in Dictionary

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].


"""
# MOWN solution
# for words ["w","wo","wor","worl","world"]
# get words map defaultdict(<type 'list'>, {u'w_': [u'wo'], u'wo_': [u'wor'], u'worl_': [u'world'], u'_': [u'w'], u'wor_': [u'worl']})

# then do recursive calls to get the world

from collections import defaultdict


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.words_map = defaultdict(list)
        for word in words:
            self.words_map[word[:-1] + '_'].append(word)

        self.result = None
        self.maxer = 0

        tresult, _ = self.get_max_word('')
        return tresult

    def get_max_word(self, word):

        if not self.words_map.has_key(word + '_'):
            return word, len(word)

        tresult = None
        tmax = 0

        for tword in self.words_map[word + '_']:
            temp_word, temp_len = self.get_max_word(tword)
            if tmax < temp_len:
                tresult, tmax = temp_word, temp_len

        return tresult, tmax