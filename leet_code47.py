"""
47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

Hide Company Tags LinkedIn Microsoft
Show Tags
Show Similar Problems

"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        def permute(nums):
            if len(nums) < 2:
                return [nums]

            elif len(nums) == 2:
                if nums[0] != nums[1]:
                    return [[nums[0], nums[1]], [nums[1], nums[0]]]
                else:
                    return [nums]

            else:
                result =list()
                for i in range(len(nums)):
                    if i > 0 and nums[i-1] == nums[i]:
                        continue

                    for perm in permute(nums[0:i] + nums[i+1:]):
                        result.append([nums[i]] + perm)

                return result

        return permute(nums)