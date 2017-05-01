"""
40. Combination Sum II

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Hide Company Tags Snapchat
Hide Tags Array Backtracking
Hide Similar Problems (M) Combination Sum
"""

# MOWN solution
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.getCombination(candidates, target)

    def getCombination(self, candidates, target):
        result = list()
        for i in range(len(candidates)):
            # Bug: Need to skip if previous element is same as current
            if i and candidates[i] == candidates[i-1]:
                continue

            if target-candidates[i] > 0:
                tresult = self.getCombination(candidates[i+1:], target-candidates[i])
                if tresult:
                    for temp in tresult:
                        result.append([candidates[i]] + temp)
            elif target-candidates[i] == 0:
                result.append([candidates[i]])

            else:
                break
        return result