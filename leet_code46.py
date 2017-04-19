"""
46. Permutations

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Hide Company Tags LinkedIn Microsoft
Hide Tags Backtracking
Hide Similar Problems (M) Next Permutation (M) Permutations II (M) Permutation Sequence (M) Combinations

"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return [nums]

        elif len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]

        else:
            result = list()
            for i in range(len(nums)):
                for perm in self.permute(nums[0:i] + nums[i+1:]):
                    result.append([nums[i]] + perm)

            return result

