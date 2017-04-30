"""
401. Binary Watch

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

Hide Company Tags Google
Hide Tags Backtracking Bit Manipulation
Hide Similar Problems (M) Letter Combinations of a Phone Number (E) Number of 1 Bits

"""
# MOWN solution backtracking
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if not num:
            return ['0:00']

        listr = ['0']*10
        result = list()
        tresult = self.getBinary(num, listr)
        for res in tresult:
            part1 = ''.join(res[:4])
            part2 = ''.join(res[4:])
            # if hour is greater than 11 or minute is greater than 59, skip it
            if int(part1, 2) > 11 or int(part2, 2) > 59:
                continue
            part1 = str(int(part1, 2))
            if int(part2, 2) < 10:
                part2 = '0' + str(int(part2, 2))

            else:
                part2 = str(int(part2, 2))

            result.append(part1 + ':' + part2)

        return result

    def getBinary(self, num, listr):
        result = list()
        for i in range(len(listr)-num+1):
            tlistr = listr[:]
            tlistr[i] = '1'
            if num != 1 and tlistr[i+1:]:
                tresult = self.getBinary(num-1, tlistr[i+1:])
                for temp in tresult:
                    result.append(tlistr[:i+1] + temp)
            else:
                result.append(tlistr)
        return result

# Dumb solution (LUP)
class Solution(object):
    def readBinaryWatch(self, num):
        result = list()
        for i in range(0, 12):
            for j in range(0, 60):
                if str(bin(i) + bin(j)).count('1') == num:
                    result.append(str(i) + ":" +  (str(j) if j > 9 else "0"+str(j)))
        return result


