"""
462. Minimum Moves to Equal Array Elements II

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

"""
# MOWN
# Solution: sort the list, get the middle element (pivot)
# all elements left of pivot should be raised and all elements right of pivot should be lowered tp pivot values

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        pivot = len(nums) / 2
        result = 0
        for i in range(len(nums)):
            if i < pivot:
                result += (nums[pivot] - nums[i])
            elif i > pivot:
                result += (nums[i] - nums[pivot])
        return result
