# coding=utf-8
"""
496. Next Greater Element I

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
Find all the next greater numbers for nums1s elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

"""
# LUP solution
# Iterate through the nums list, Use stack to save all the descending sub sequence of numbers from nums
# everytime you hit higher number, that will the greatest number for the nums in stack that are,
# less than the number (so we pop all of them out and put it into a map)
# for example if I have nums = [9, 8, 7, 3, 2, 1, 6] then my stack will have [9, 8, 7, 3, 2, 1],
# now during the iteration for num 6 we see that 1 < 6, hence next greatest for 1 is 6, similarly for 2 and 3

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack, mapr, result = list(), dict(), list()

        for num in nums:
            while stack and stack[-1] < num:
                mapr[stack.pop()] = num

            stack.append(num)

        for num in findNums:
            result.append(mapr[num] if mapr.has_key(num) else -1)

        return result