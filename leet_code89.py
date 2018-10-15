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
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]

        else:
            o_list, i_list = ['0'], ['1']
            for i in range(2, n + 1):
                to_list, ti_list = list(), list()
                for num in o_list + i_list:
                    to_list.append('0' + num)
                    ti_list.append('1' + num)

                o_list, i_list = to_list, ti_list[::-1]

            return map(lambda x: int(x, 2), o_list + i_list)