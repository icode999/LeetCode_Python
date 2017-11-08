"""
127 Word Ladder 

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

"""
# LUP Solution
# Build a map with the given words
# {'jk_': ['jkl'], 'de_': ['def'], 'gh_': ['ghi'], 'j_l': ['jkl'], '_ef': ['def'], '_kl': ['jkl'], 'a_c': ['abc'], '_hi': ['ghi'], 'g_i': ['ghi'], 'd_f': ['def'], '_bc': ['abc'], 'ab_': ['abc']}

# Now do BFS with words using queue. (word, count)
from collections import defaultdict, deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        words_map = self.get_words_map(wordList)
        return self.bfs_words(beginWord, endWord, words_map)

    def bfs_words(self, begin, end, words_map):
        visited, queue = set(), deque([(begin, 1)])

        while queue:
            word, count = queue.popleft()
            if word not in visited:
                visited.add(word)

                if word == end:
                    return count

                for i in range(len(word)):
                    temp = word[:i] + "_" + word[i + 1:]
                    listr = words_map[temp] if words_map.has_key(temp) else []
                    for tword in listr:
                        queue.append((tword, count + 1))

        return 0

    def get_words_map(self, wordList):
        mapr = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                tword = word[:i] + "_" + word[i + 1:]
                mapr[tword].append(word)

        return mapr