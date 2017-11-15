"""
36. Valid Sudoku

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

"""
# LUP
# Save everything to set, for each element we save
# row(value)
# (value)col
# row_quad(value)(col_quad)

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        exists = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue

                tstr = "(%s)" % board[i][j]
                if (str(i) + tstr) in exists or (tstr + str(j)) in exists or (str(i / 3) + tstr + str(j / 3)) in exists:
                    return False

                exists.add(str(i) + tstr)
                exists.add(tstr + str(j))
                exists.add(str(i / 3) + tstr + str(j / 3))

        return True