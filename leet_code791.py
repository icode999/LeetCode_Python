"""
791. Custom Sort String

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.


Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.

Companies
Google
"""
# MOWN
# build a map of T
# iterate through S and populate result if char exists in T (populate all of them)
# populate the rest of the chars from T

from collections import Counter
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        result = ""
        Tc = Counter(T)
        for char in S:
            if char in Tc:
                result += char * Tc[char]  # populate all of the Bug "kqep" - "pekeq"
                Tc[char] = 0

        for key, value in Tc.iteritems():
            result += key * value

        return result