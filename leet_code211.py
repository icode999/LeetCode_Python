"""
211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

click to show hint.

Hide Company Tags Facebook
Hide Tags Backtracking Trie Design
Hide Similar Problems (M) Implement Trie (Prefix Tree)
"""
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapr = dict()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        mapr = self.mapr
        for char in word:
            if mapr.has_key(char):
                mapr = mapr[char]
            else:
                mapr[char] = dict()
                mapr = mapr[char]
        mapr['EOW'] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        mapr = self.mapr
        return self._search(word, 0, mapr)

    def _search(self, word, i, mapr):
        if i == len(word):
            if mapr and mapr.has_key('EOW'): # Bug : Check for EOW
                return True
            else:
                return False

        if word[i] == '.':
            for key in mapr.keys():
                if key != 'EOW':
                    return self._search(word, i+1, mapr[key])
            return False
        else:
            if word[i] in mapr.keys():
                return self._search(word, i+1, mapr[word[i]])
            else:
                return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)