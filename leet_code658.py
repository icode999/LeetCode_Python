"""
658. Find K Closest Elements

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

Companies
Google 2Amazon 2LinkedIn 2

"""
# MOWN use binary search to find pos and then use two pointers
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        def get_best_index():
            low = 0
            high = len(arr) - 1

            while low < high:
                mid = (low + high) >> 1
                if arr[mid] > x:
                    high = mid
                else:
                    low = mid + 1
            return low

        index = get_best_index()
        result = list()
        i = index-1
        j = index
        for _ in range(k):
            if i >= 0 and j < len(arr):
                if abs(x - arr[i]) <= abs(x - arr[j]):
                    result.append(arr[i])
                    i -= 1
                else:
                    result.append(arr[j])
                    j += 1
            else:
                if i < 0:
                    result.append(arr[j])
                    j += 1
                else:
                    result.append(arr[i])
                    i -= 1

        return sorted(result)


# LUP Binary search
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        low = 0
        high = len(arr) - k

        while low < high:
            mid = (low + high) >> 1
            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1
            else:
                high = mid

        return arr[low:low + k]
