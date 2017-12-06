"""
556. Next Greater Element III

Given a positive 32-bit integer n, you need to find the smallest 32-bit 
integer which has exactly the same digits existing in the integer n and is greater in value than n. 
If no such positive 32-bit integer exists, you need to return -1.

Example 1:
Input: 12
Output: 21
Example 2:
Input: 21
Output: -1

Companies 
Bloomberg 

"""
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = str(n)
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                temp = list(num[i:])
                for j in range(len(temp)-1, 0, -1):
                    if temp[0] < temp[j]:
                        key = temp[j]
                        temp = temp[:j] + temp[j+1:]
                        temp.sort()
                        res = int(num[:i] + key + ''.join(temp))
                        return res if res <= (2**31-1) else -1
        return -1