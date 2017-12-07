"""
657. Judge Route Circle

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, 
judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. 
The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false

Companies
Google
"""
# MOWN solution using collections.Counter
# Counter['T'] will be 0 by default as it doesnt exist

from collections import Counter
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        counter = Counter(moves)
        return True if (counter["U"] == counter["D"]  and counter["L"] == counter["R"]) else False