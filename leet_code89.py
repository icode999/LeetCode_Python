"""
89. Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

"""
# LUP
# when n=3, we can get the result based on n=2.
# 00,01,11,10 -> (000,001,011,010 ) (110,111,101,100).

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if not n:
            return [0]

        return map(lambda num: int(num, 2), self.Helper(['0', '1'], n))

    def Helper(self, bin_list, iter):
        if not iter:
            return None

        tresult = self.Helper(bin_list, iter - 1)
        result = list()
        if not tresult:
            result = bin_list[:]

        else:
            for num in bin_list:
                if num == '1':
                    tresult = tresult[::-1]  # this is critical in this
                for res in tresult:
                    result.append(num + res)

        return result