
"""
651. 4 Keys Keyboard

Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

Example 1:
Input: N = 3
Output: 3
Explanation: 
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A
Example 2:
Input: N = 7
Output: 9
Explanation: 
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
Note:
1 <= N <= 50
Answers will be in the range of 32-bit signed integer.


Companies : Google Microsoft 

Solution: 

best[k] = max(best[k-1] + 1, best[k-2] * 1, best[k-3] * 2, best[k-4] * 3, ...)
"""


class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        best = [0, 1]
        for i in range(2, N + 1):
            result = max(best[i - 1] + 1, best[i - 2] + 2)

            for j in range(i - 3, -1, -1):
                result = max(result, best[j] * (i - j - 1))

            best.append(result)

        return best[-1]