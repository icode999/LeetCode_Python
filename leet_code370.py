"""
370. Range Addition

Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Given:

    length = 5,
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]

Output:

    [-2, 0, 3, 5, 3]
Explanation:

Initial state:
[ 0, 0, 0, 0, 0 ]

After applying operation [1, 3, 2]:
[ 0, 2, 2, 2, 0 ]

After applying operation [2, 4, 3]:
[ 0, 2, 5, 5, 3 ]

After applying operation [0, 2, -2]:
[-2, 0, 3, 5, 3 ]
Credits:
Special thanks to @vinod23 for adding this problem and creating all test cases.

Hide Company Tags Google
Show Tags
"""
# MOWN
# o(n+k) time and o(n) space
from collections import defaultdict
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        dict_start = defaultdict(int)
        dict_end = defaultdict(int)

        # Bug initially: you have add each update as there can be multiple updates start or end at same index
        # for example: [1, 139, -29]    &   [1, 37, 47]   here both start at index 1 so value needs to be 18  (47+(-29))
        for update in updates:
            dict_start[update[0]] += update[2]
            dict_end[update[1]+1] += update[2]

        result = list()
        prev_sum = 0
        for i in range(length):
            if dict_start.has_key(i):
                prev_sum += dict_start[i]

            if dict_end.has_key(i):
                prev_sum -= dict_end[i]

            result.append(prev_sum)

        return result


# LUP Solution
# similar to MOWN solution but instead of maintaining mapr for start and end index we update the list itself
# as add value to startend and subtract value to endindex + 1

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        result = [0]*(length + 1)
        for update in updates:
            result[update[0]] += update[-1]
            result[update[1]+1] -= update[-1]

        for i in range(1, length):
            result[i] += result[i-1]

        return result[:-1]