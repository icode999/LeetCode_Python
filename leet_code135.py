# -*- coding: utf-8 -*-
"""
135.Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.

Companies   
Google 11 Uber 2           
"""
# LUP 
# Do left2right and L2R[i] += L2R[i-1] if ratings[i] > ratings[i-1]
# Do right2left and R2L[i] += R2L[i+1] if ratings[i] > ratings[i+1]
# result is max(L2R[i], R2L[i])
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        L2R = [1]*len(ratings)
        R2L = [1]*len(ratings)
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                L2R[i] += L2R[i-1]

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                R2L[i] += R2L[i+1]
            
            L2R[i] = max(L2R[i], R2L[i])

        return sum(L2R)
