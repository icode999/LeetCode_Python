"""
130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Hide Tags Breadth-first Search Union Find
Show Similar Problems


"""
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.

        Solution: we populate 'O' that are on the border and then expand to neighbours and mark them a T
        At the end we change all T to O and remaining O to X
        """
        stack = list()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row in [0, len(board)-1] or col in [0, len(board[0])-1]) and board[row][col] == 'O':
                    stack.append([row, col])

        while stack:
            row, col = stack.pop()
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'O':
                board[row][col] = "T"

                for neighbour in [[row+1, col], [row-1, col], [row, col-1], [row, col+1]]:
                    stack.append(neighbour)


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != 'X':
                    board[row][col] = ['O', 'X'][board[row][col] == 'O']
