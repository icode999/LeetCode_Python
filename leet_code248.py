"""
248. Strobogrammatic Number III

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

For example,
Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.

Note:
Because the range might be a large number, the low and high numbers are represented as string.

Hide Tags Math Recursion
Show Similar Problems

"""
class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        if int(low) == int(high):
            return 1
        elif int(low) > int(high):
            return 0

        result = 0
        for i in range(len(low), len(high)+1):
            tresult = self.strobogrammatic(i)
            #print tresult

            if len(low) == len(high):
                for j in range(len(tresult)):
                    if int(low) <= int(tresult[j]) <= int(high):
                        result += 1

            elif i == len(low):
                for j in range(len(tresult)):
                    if int(tresult[j]) >= int(low):
                        break
                result += len(tresult[j:])

            elif i == len(high):
                for j in range(len(tresult)):
                    if int(tresult[j]) <= int(high):
                        result += 1
                    else:
                        break
            else:
                result += len(tresult)
        return result

    def strobogrammatic(self, n):
        one = ['0', '1', '8']
        two = ["00", "11","69","88","96"]
        if n == 1:
            return one
        elif n == 2:
            return two[1:]

        else:
            if n % 2:
                lista = self.strobogrammatic(n-1)
                listb = one[:]
            else:
                lista = self.strobogrammatic(n-2)
                listb = two[:]

            result = [i[:len(i)/2] + j + i[len(i)/2:] for i in lista for j in listb]
            return result
