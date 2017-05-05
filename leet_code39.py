"""
39. Combination Sum

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]

Hide Company Tags Snapchat Uber
Hide Tags Array Backtracking
Hide Similar Problems (M) Letter Combinations of a Phone Number (M) Combination Sum II (M) Combinations (M) Combination Sum III (M) Factor Combinations (M) Combination Sum IV
"""

# MOWN solution
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()  # Bug: Did not sort, need sort because for test case [4,2,8]  8
        # W/O sort : [[4,4],[2,2,2,2],[8]], expected O/P is: [[2,2,2,2],[2,2,4],[4,4],[8]]
        return self.getcomb(candidates, target)

    def getcomb(self, candidates, target):
        if target < 0:
            return []

        result = list()
        count = -1
        for num in candidates:
            count += 1
            if target-num == 0:
                result.append([num])
                break

            if target-num > 0:
                tresult = self.combinationSum(candidates[count:], target-num)
                if tresult:
                    for temp in tresult:
                        result.append([num]+temp)

        return result