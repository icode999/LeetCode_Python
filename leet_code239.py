"""
239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 <= k <= input arrays size for non-empty array.

Follow up:
Could you solve it in linear time?

Hint:

How about using a data structure such as deque (double-ended queue)?
The queue size need not be the same as the window's size.
Remove redundant elements and the queue should store only elements that need to be considered.


Hide Company Tags Amazon Google Zenefits
Show Tags
Show Similar Problems

"""


'''
Keep indexes of good candidates in deque d. The indexes in d are from the current window, they're increasing, and their corresponding nums are decreasing. Then the first deque element is the index of the largest window value.

For each index i:

Pop (from the end) indexes of smaller elements (they'll be useless).
Append the current index.
Pop (from the front) the index i - k, if it's still in the deque (it falls out of the window).
If our window has reached size k, append the current window maximum to the output.
'''

# LUP Solution
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return nums
        window, result = deque(), list()
        for i in range(len(nums)):
            while window and nums[window[-1]] < nums[i]:
                window.pop()

            window.append(i)
            if window[0] <= i-k:
                window.popleft()

            if i >= k-1:
                result.append(nums[window[0]])

        return result