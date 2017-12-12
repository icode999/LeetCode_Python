"""
277. Find the Celebrity

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. 
The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. 
The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. 
You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. 
Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. 
Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

"""
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

# MOWN Solution
# for each person we check if he is known by everyone else (while we do that we update our dp list)
# two updates: 1) for everyonelse if they know current person, we update that "everyone" person is not celebirty
# 2) if everyone else doesnt know we update current person as not celebrity

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1] * n
        for idx in range(n):
            if not result[idx]:
                continue

            for nei in range(0, idx) + range(idx + 1, n):
                if not knows(nei, idx):
                    result[idx] = 0
                    break
                else:
                    result[nei] = 0

                if knows(idx, nei):
                    result[idx] = 0
                    break

        for idx in range(n):
            if result[idx]:
                return idx

        return -1