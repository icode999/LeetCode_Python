"""
216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

"""

# MOWN Solution
# keep track of k, break if k number is not reached

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.Helper(range(1, 10), n, k)

    def Helper(self, nums, target, k):
        if target < 0:
            return []

        result = list()
        for i, num in enumerate(nums):
            if target - num == 0:
                if k == 1:
                    result.append([num])
                else:
                    break

            elif target - num > 0:
                tresult = self.Helper(nums[i + 1:], target - num, k - 1)
                for tres in tresult:
                    result.append([num] + tres)

            else:
                break

        return result