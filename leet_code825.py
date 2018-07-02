"""
825. Friends Of Appropriate Ages

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person.

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 100...6, 18 -> 17.
Example 3:

Input: [20,30,100,110,120]
Output:
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.


Notes:

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.

Companies
Facebook
"""
# LUP solution
# 1st and 2nd condition can be combined as below
# A can send friend request to B if and only if 0.5*A + 7 < B <= A
# that means 0.5*A + 7 < A which means A > 14
# So we start from 14. Given that 1 <= ages[i] <= 120, we count all the people in each age
# For each pair (ageA, countA), (ageB, countB), if the conditions are satisfied with respect to age, then countA * countB pairs of people made friend requests.
# If ageA == ageB, then we overcounted: we should have countA * (countA - 1)
# hence we start A from 14 to 121 and B from 0.5*A + 7 to A and multiply counts and add to result


from collections import defaultdict


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        mapr = defaultdict(int)
        for age in ages:
            mapr[age] += 1

        result = 0
        for i in range(15, 121):
            for j in range(int(0.5 * i) + 8, i + 1):
                if i == j:
                    result += mapr[i] * (mapr[i] - 1)
                else:
                    result += mapr[i] * mapr[j]

        return result
