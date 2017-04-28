"""
447. Number of Boomerangs

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
Hide Company Tags Google
Hide Tags Hash Table
Hide Similar Problems (M) Line Reflection

"""

# MOWN Solution got TLE and pretty complex
from collections import defaultdict
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        mapr = defaultdict()
        for i in range(len(points)):
            tmapr = defaultdict(list)
            mapr[i] = tmapr

        def get_distance(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return dx*dx + dy*dy

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = get_distance(points[i], points[j])
                mapr[i][dist].append(j)
                mapr[j][dist].append(i)

        result = 0
        for key, value in mapr.iteritems():
            for tkey, tvalue in value.iteritems():
                if len(tvalue) > 1:
                    for i in range(len(tvalue)):
                        for j in range(i+1, len(tvalue)):
                            result += 2
        return result

# LUP Solution
# Solution: maintain a map with distance as key and value as count
# for everypoint we iterate through all points and populate our map
# at each point we calculate the number combinations (n*n-1) and add it to the result

from collections import defaultdict
class Solution(object):
    def numberOfBoomerangs(self, points):
        result = 0
        for p1 in points:
            mapr = defaultdict(int)
            for p2 in points:
                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]
                mapr[dx*dx + dy*dy] += 1

            result += sum(value*(value-1) for value in mapr.values())
        return result
