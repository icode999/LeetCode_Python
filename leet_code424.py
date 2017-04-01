"""
424. Longest Repeating Character Replacement

Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
Hide Company Tags Pocket Gems
Show Similar Problems

"""

#OWN SOL
# Solution: Sliding window, we have to make sure that our window should have  k or less distinct chars
# if distinct chars is more than k we shrink the window by 1 (No need to shrink it untill we get k distinct chars)
"""
StefanPochmann
I don't think you need while, because from one for-loop iteration to the next, hi - lo - max_char_n + 1 can grow by at most 1, and each while-loop iteration decreases it by 1.
 So you can also use if instead. It also means that your window never shrinks, so you can just return the length of the final window:

"""

from collections import Counter
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        lo, hi, mapr, maxer = 0, 0, Counter(), 0
        for hi in range(1, len(s)+1):
            mapr[s[hi-1]] += 1
            maxer = mapr.most_common(1)[0][1]
            if hi - lo - maxer > k:
                mapr[s[lo]] -= 1
                lo += 1

        return hi - lo
