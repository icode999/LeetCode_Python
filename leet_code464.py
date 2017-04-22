"""
464. Can I Win

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

Hide Company Tags LinkedIn
Hide Tags Dynamic Programming Minimax
Show Similar Problems
"""
# LUP Solution, memoization while checking if player2 can win with each number out of the list (since player will select the 1st number)

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if maxChoosableInteger*(maxChoosableInteger + 1)/2 < desiredTotal:
            return False

        self.dp = dict()
        return self.memoization(range(1, maxChoosableInteger+1), desiredTotal)

    def memoization(self, nums_list, summ):
        hash = str(nums_list)
        if self.dp.has_key(hash):
            return self.dp[hash]

        if summ <= nums_list[-1]:
            self.dp[hash] = True
            return True

        for i in range(len(nums_list)):
            if not self.memoization(nums_list[:i] + nums_list[i+1:], summ-nums_list[i]):
                self.dp[hash] = True
                return True

        self.dp[hash] = False
        return False