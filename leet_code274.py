"""
274. H-Index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of hindex on Wikipedia"A scientist has index h if h of his/her N papers have at least h citations each, and the other N - h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Hint:

An easy approach is to sort the array first.
What are the possible values of h-index?
A faster approach is to use extra space.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Hide Company Tags Bloomberg Google Facebook
Show Tags
Show Similar Problems
"""

# Looked up solution
'''
Solution:  It is easy to solve if we sort the array, But there is O(n) solution

The max H-index can go is n (where n is the length of the citation array)
So we create a temp array (Index of this array specify H-index) and if any citation is greater than n we increment temp_arry[n] else we increment the temp_array[i]
where i is the current iterating index.

Now we read the array from the backwards and at any point of the count of papers increase by index we return

https://discuss.leetcode.com/topic/40765/java-bucket-sort-o-n-solution-with-detail-explanation/2

'''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        result_arr = [0]*(n+1)

        for i in range(n):
            if citations[i] >= n:
                result_arr[n] += 1
            else:
                result_arr[citations[i]] += 1

        i, result = n, 0
        while i > 0:
            result += result_arr[i]
            if result >= i:
                return i
            else:
                i -= 1
        return 0
