"""
487. Max Consecutive Ones II

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

Hide Company Tags Google
Show Tags
Show Similar Problems

"""
# Missed testcase when all elements are 1's
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count1, count2, flag, maxer = 0, 0, 0, 0  # we need flag to handle all 1's case where we dont need to flip any 0
        for num in nums:
            if num == 1:
                count2 += 1
            else:
                maxer = max(count1+count2, maxer)
                count1, count2, flag = count2, 0, 1

        maxer = max(count1+count2, maxer)
        return maxer+flag
