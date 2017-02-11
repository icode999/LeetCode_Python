"""
Given a non negative integer number num. For every numbers i in the range 0 <= i <= num calculate the number of 1s in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

"""

import math
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        power_counter = 0
        power_num = math.pow(2, power_counter)

        for i in range(1, num+1):
            if power_num == i:
                result.append(1)
                power_counter += 1
                power_num = int(math.pow(2, power_counter))
            else:
                result.append(1+ result[i-power_num])

        return result


# little optimization that reduces run time
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        power_counter = 0

        for i in range(1, num+1):
            if i&i-1 == 0:   # check if number is power of 2
                result.append(1)
                power_counter = i  # save it if number is power of 2
            else:
                result.append(1+ result[i-power_counter]) # result is just 1+ result[i-last saved power of 2]

        return result
