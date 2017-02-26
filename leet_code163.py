"""
163. Missing Ranges

Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

Hide Company Tags Google


Some of the test cases
[0,1,3,50,75]
0
99
[3,50,75]
0
99
[3,50,75, 120]
0
99
[0]
0
99
[]
1
100
[]
1
1
[-1]
-1
-1
[1,1,1]
1
1
[1,1,1]
1
100
"""
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums: # Missed this test case if nums is empty list
            return [str(lower) if lower==upper else str(lower) + "->" + str(upper)]

        low = lower-1
        result = list()
        for num in nums:
            if low == num:   # Missed this testcase if there are duplicates
                continue
            if low + 1 != num:
                result.append(str(low+1) if low+1 == num-1 else str(low+1) + "->" + str(num-1))
            low = num

        if num < upper:
            result.append(str(num+1) if num+1 == upper else str(num+1) + "->" + str(upper))

        return result
