"""
212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

Hide Company Tags Microsoft Google Airbnb
Hide Tags Backtracking Trie
Show Similar Problems


"""

# LUP Solution

# Build a trie for words and pass that trie to find method and do DFS
# everytime end trie is reached append the word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return []

        self.words = words
        self.board = board
        self.build_trie()
        self.result = list()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(i, j, self.trie, '')

        return list(set(self.result))


    def find(self, i, j, trie, pword):
        if trie.has_key('#'):
            self.result.append(pword)

        if 0 <= i < len(self.board) and 0 <= j < len(self.board[0]) and trie.has_key(self.board[i][j]):
            temp = self.board[i][j]
            self.board[i][j] = '*'
            for ti, tj in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                self.find(ti, tj, trie[temp], pword+temp)

            self.board[i][j] = temp
        return

    def build_trie(self):
        # instead of using regular trie we just create a dict
        self.trie = dict()
        for word in self.words:
            trie = self.trie

            for char in word:
                if not trie.has_key(char):
                    trie[char] = dict()

                trie = trie[char]

            # represent end of the word
            trie['#'] = '#'
