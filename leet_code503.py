"""
503. Next Greater Element II

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

"""


# MOWN solution after LUP Next Greater Element I
# Instead of saving into mapr we directly update the result list
# Since this is circular I iterate through the nums twice back 2 back

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result, stack = [-1] * len(nums), list()

        for idx, num in enumerate(nums + nums):
            while stack and stack[-1][-1] < num:
                tidx, tnum = stack.pop()
                tidx = tidx % len(nums)
                result[tidx] = num

            stack.append([idx, num])

        return result