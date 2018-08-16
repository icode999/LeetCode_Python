"""
846. Hand of Straights

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.



Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.


Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length

Companies
Google
"""
# MOWN
# count the frequency
# sort the keys based on key
# iterate through W consecutive keys

from collections import Counter
class Solution(object):
    def isNStraightHand(self, listr, W):
        if len(listr) % W != 0:
            return False

        mapr = Counter(listr)
        keys = mapr.keys()
        keys.sort()

        for key in keys:
            while mapr[key] > 0:
                for i in range(W):
                    if key + i in mapr:
                        mapr[key + i] -= 1
                        if mapr[key + i] == 0:
                            mapr.pop(key + i)
                    else:
                        return False

        return len(mapr) == 0
