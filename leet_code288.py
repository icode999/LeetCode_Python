"""
228. Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Hide Company Tags Google
Show Tags
Show Similar Problems

"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums

        low = nums[0]
        current = nums[0]
        result = list()
        flag = True

        for num in nums[1:]:
            if current+1 != num:
                result.append(str(low) if low == current else str(low) + "->" + str(current))
                low = num
                current = num
                flag = False
            else:
                flag = True
                current = num
        result.append(str(low) if low == current else str(low) + "->" + str(current))
        return result
