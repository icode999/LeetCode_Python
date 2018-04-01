"""
423. Reconstruct Original Digits from English

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"

"""
# LUP Solution
# look for letters that are unique to specific digits
# then get the rest based on that
from collections import defaultdict


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        mapr = defaultdict(int)
        for letter in s:
            if letter == 'x':
                mapr[6] += 1

            elif letter == 'w':
                mapr[2] += 1

            elif letter == 'z':
                mapr[0] += 1

            elif letter == 'g':
                mapr[8] += 1

            elif letter == 'u':
                mapr[4] += 1

            elif letter == 'f':  # 5-4
                mapr[5] += 1

            elif letter == 'i':  # 9-8-6-5
                mapr[9] += 1

            elif letter == 'v':  # 7-5
                mapr[7] += 1

            elif letter == 'h':  # 3-8
                mapr[3] += 1

            elif letter == 'o':  # 1-0-2-4
                mapr[1] += 1

        mapr[5] -= mapr[4]
        mapr[9] -= mapr[8] + mapr[6] + mapr[5]
        mapr[7] -= mapr[5]
        mapr[3] -= mapr[8]
        mapr[1] -= mapr[0] + mapr[2] + mapr[4]

        result = ''
        for i in range(10):
            result += str(i) * mapr[i] if mapr[i] > 0 else ''

        return result