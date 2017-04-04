"""
246. Strobogrammatic Number

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

Hide Company Tags Google
Show Tags
Show Similar Problems


"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mapr = {'8':'8', '9':'6', '6':'9', '1':'1', '0':'0'}
        temp = ''
        for char in num:
            if mapr.has_key(char):
                temp = mapr[char] + temp
            else:
                return False
        return num == temp

