"""
208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

Hide Company Tags Google Uber Facebook Twitter Microsoft Bloomberg
Hide Tags Design Trie
Hide Similar Problems (M) Add and Search Word - Data structure design
"""
class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapr = dict()

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        mapr = self.mapr
        for char in word:
            if not mapr.has_key(char):
                return False
            mapr = mapr[char]
        return True if mapr.has_key('EOW') else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        mapr = self.mapr
        for char in prefix:
            if not mapr.has_key(char):
                return False
            mapr = mapr[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)