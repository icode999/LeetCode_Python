"""
247. Strobogrammatic Number II

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].

Hint:

Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.
Hide Company Tags Google
Show Tags
Show Similar Problems

"""

"""
n == 1: [0, 1, 8]

n == 2: [11, 88, 69, 96]

How about n == 3?
=> it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 2

n == 4?
=> it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 2

n == 5?
=> it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 4

the same, for n == 6, it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 4

"""
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        one = ['0', '1', '8']
        two = ["00", "11","69","88","96"]
        if n == 1:
            return one
        elif n == 2:
            return two[1:]

        else:
            if n % 2:
                lista = self.findStrobogrammatic(n-1)
                listb = one[:]
            else:
                lista = self.findStrobogrammatic(n-2)
                listb = two[:]

            result = [i[:len(i)/2] + j + i[len(i)/2:] for i in lista for j in listb]
            return result

