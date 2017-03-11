"""
249. Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

Hide Company Tags Google Uber
Hide Tags Hash Table String
Show Similar Problems

"""

from collections import defaultdict
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        mapr = defaultdict(list)
        for string in strings:
            if not string:
                mapr[""].append(string)
                continue
            temp = '0'
            char = ord(string[0])
            for item in string[1:]:
                temp += str((char - ord(item))%26)
                char = ord(item)

            mapr[temp].append(string)

        return mapr.values()