"""
90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Companies
Facebook

"""
# LUP
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        nums.sort()
        for idx, num in enumerate(nums):
            if idx == 0 or nums[idx] != nums[idx - 1]:
                count = len(result)

            result += [res + [num] for res in result[-count:]]

        return result