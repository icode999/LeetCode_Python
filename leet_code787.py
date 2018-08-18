"""
787. Cheapest Flights Within K Stops

There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and fights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.

Companies
Google
"""

# DFS (partial LUP)
from collections import defaultdict
class Solution(object):
    def findCheapestPrice(self, n, flights, osrc, odst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        self.result = float('inf')
        self.flights_map = defaultdict(list)

        for flight in flights:
            self.flights_map[flight[0]].append(flight[1:])

        def DFS(src, cost, distance):
            if distance > K:
                return
            if src == odst:
                self.result = min(self.result, cost)
                return
            distance += 1
            for tflight in self.flights_map[src]:
                if tflight[1] + cost > self.result:
                    continue

                DFS(tflight[0], tflight[1] + cost, distance)
            return

        DFS(osrc, 0, -1)
        return self.result if self.result != float('inf') else -1


# BFS
from collections import defaultdict, deque


class Solution(object):
    def findCheapestPrice(self, n, flights, osrc, odst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        self.result = float('inf')
        self.flights_map = defaultdict(list)

        for flight in flights:
            self.flights_map[flight[0]].append(flight[1:] + [0])

        que = deque([[osrc, 0, -1]])
        while que:
            node = que.popleft()
            if node[0] == odst:
                self.result = min(self.result, node[1])
                continue

            distance = node[2] + 1
            for tnode in self.flights_map[node[0]]:
                next_cost = tnode[1] + node[1]
                if next_cost > self.result or distance > K:
                    continue

                que.append([tnode[0], next_cost, distance])

        return self.result if self.result != float('inf') else -1
