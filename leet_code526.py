"""
526. Beautiful Arrangement

Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

Example 1:
Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
Note:
N is a positive integer and will not exceed 15.

"""

# LUP got TLE
class Solution(object):
    def __init__(self):
        self.count = 0

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if not N:
            return self.count
        used_list = [0] * (N + 1)
        self.get_counter(N, 1, used_list)
        return self.count

    def get_counter(self, N, position, used_list):
        if position == N + 1:
            self.count += 1
            return

        for i in range(1, N + 1):
            if used_list[i] == 0 and (i % position == 0 or position % i == 0):
                used_list[i] = 1
                self.get_counter(N, position + 1, used_list)
                used_list[i] = 0
        return


# LUP Accepted
# https://discuss.leetcode.com/topic/82141/java-6ms-beats-98-back-tracking-swap-starting-from-the-back

class Solution(object):
    def __init__(self):
        self.counter = 0

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 3:
            return N

        nums = range(N + 1)
        self.Helper(nums, N)
        return self.counter

    def Helper(self, nums, start):
        if start == 0:
            self.counter += 1
            return

        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        for i in range(start, 0, -1):
            swap(nums, start, i)
            if nums[start] % start == 0 or start % nums[start] == 0:
                self.Helper(nums, start - 1)

            swap(nums, i, start)

        return









