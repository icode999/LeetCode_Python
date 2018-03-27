"""
491. Increasing Subsequences

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

Companies 
Yahoo

"""
class Solution(object):
    def findSubsequences(self, nums):
        result = list()
        lenn = len(nums)

        def DFS(current, i):
            print current, i
            if len(current) > 1:
                result.append(current)

            visited = list()
            for j in range(i + 1, lenn):
                if i >= 0 and nums[j] < nums[i] or nums[j] in visited:
                    continue
                DFS(current + [nums[j]], j)

                visited.append(nums[j])

        DFS([], -1)
        return result
