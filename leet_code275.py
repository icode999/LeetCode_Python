"""
Follow up for H-Index (leet code 274): What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hide Company Tags Facebook
Hide Tags Binary Search
Hide Similar Problems (M) H-Index

"""

# MOWN Solution
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        counter = 0
        for i in citations[::-1]:
            counter += 1
            if i >= counter:
                continue
            else:
                break
        else:
            return counter
        return counter -1

class Solution(object):
    def hIndex(self, citations):
        counter, i = 0, len(citations)-1
        while i >= 0:
            counter += 1
            temp = citations[i]
            i -= 1
            if temp < counter:
                break
        else:
            return counter
        return counter-1

# LUP solution
# Binary search
class Solution(object):
    def hIndex(self, citations):
        low, high, lenc = 0, len(citations) -1, len(citations)
        while low <= high:
            mid = (low+high)/2
            if citations[mid] == lenc - mid:
                return citations[mid]

            elif citations[mid] > lenc - mid:
                high = mid - 1

            else:
                low = mid + 1

        return lenc - low
