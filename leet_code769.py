"""
769. Max Chunks To Make Sorted

Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
Note:

arr will have length in range [1, 10].
arr[i] will be a permutation of [0, 1, ..., arr.length - 1].

Companies
Google
"""

# MOWN
# keep track of max and maintain a counter, for every element below the max decrement the counter
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        current_max, current_min = arr[0], 0
        current_count = current_max - current_min

        result = 1
        for num in arr[1:]:
            if current_count == 0:
                result += 1
                current_min, current_max = current_max, num
                current_count = current_max - current_min - 1
                continue

            if num < current_max:
                current_count -= 1

            else:
                current_count += num - current_max - 1
                current_max = num

        return result

# LUP

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        current_max = 0
        result = 0
        for idx, num in enumerate(arr):
            current_max = max(current_max, num)
            if idx == current_max:
                result += 1
        return result