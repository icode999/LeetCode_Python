"""
524. Longest Word in Dictionary through Deleting

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.

Hide Company Tags Google
Hide Tags Two Pointers Sort

"""

# MOWN
# Solution: Sort d and for each word in d see if it exists in s
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def cmpp(a, b):
            if len(a) > len(b):
                return -1
            elif len(a) < len(b):
                return 1
            else:
                return 1 if a > b else -1

        d = sorted(d, cmp=cmpp)
        #print d

        for word in d:
            si = iter(s)
            if all(char in si for char in word):
                return word
        return ''

# LUP
class Solution(object):
    def findLongestWord(self, s, d):
        for word in sorted(d, key=lambda w:(-len(w), w)):
            si = iter(s)
            if all(char in si for char in word):
                return word
        return ''