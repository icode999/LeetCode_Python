"""
242. Valid Anagram

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Hide Company Tags Amazon Uber Yelp
Hide Tags Hash Table Sort
Hide Similar Problems (M) Group Anagrams (E) Palindrome Permutation (E) Find All Anagrams in a String


"""

from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapr = defaultdict(int)
        for char in s:
            mapr[char] += 1

        for char in t:
            mapr[char] -= 1

        result = list(set(mapr.values()))
        # need to make sure number of elements in set is 0 or 1, if there is 1 element it should be 0 for anagram
        return len(result) == 0 or (len(result) == 1 and result[0] == 0)

# solution 2
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
