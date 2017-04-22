"""
294. Flip Game II

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.

Hide Company Tags Google
Hide Tags Backtracking
Hide Similar Problems (E) Nim Game (E) Flip Game (M) Guess Number Higher or Lower II (M) Can I Win

"""
# LUP (got idea first, but LUP)
# Solution: Backtracking, for every ++ we change it -- and see if the second player can win
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False
        current = 0
        for i in range(1, len(s)):
            if s[current: i+1] == "++":
                if not(self.canWin(s[:current] + '--' + s[i+1:])):
                    return True
            current += 1
        return False