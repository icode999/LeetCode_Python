"""
551. Student Attendance Record I

You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False

Hide Company Tags Google
Hide Tags String
Show Similar Problems

"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = False
        l = 0
        for i in s:
            if i == "A":
                l = 0
                if a:
                    return False
                else:
                    a = True
            elif i == "L":
                l += 1
                if l > 2 :
                    return False
            else:
                l = 0

        return True

import re
class Solution(object):
    def checkRecord(self, s):
        if re.search("A.*A|LLL", s):
            return False
        else:
            return True

