"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

Hide Company Tags Microsoft Bloomberg Facebook
Hide Tags Array Backtracking
Show Similar Problems
"""

class Solution:
    def exist(self, board, word):
        if not board or not word:
            return False
        self.visited = [[0]*len(board[0]) for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                 if board[i][j] == word[0] and not self.visited[i][j]:
                    result = self.dfs(board, i, j, word[1:])
                    if result:
                        return result
        return False

    def get_valid_neighbours(self, board, i, j):
        result = list()
        for x, y in [[i, j-1], [i, j+1], [i-1, j], [i+1, j]]:
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and not self.visited[x][y]:
                result.append([x, y])
        #print result
        return result

    def dfs(self, board, i, j, word):
        if not word:
            return True
        self.visited[i][j] = 1
        neighbours = self.get_valid_neighbours(board, i, j)
        #print neighbours
        for neighbour in neighbours:
            if board[neighbour[0]][neighbour[1]] == word[0]:
                result = self.dfs(board, neighbour[0], neighbour[1], word[1:])

                if result:
                    return result
        self.visited[i][j] = 0   # changing this back to not visited is really important
        return False