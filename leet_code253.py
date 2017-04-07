"""
253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

Hide Company Tags Google Snapchat Facebook
Show Tags
Show Similar Problems

"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heapq

# Use min heap, everytime check if the least meeting end time is less than current meeting start time (no room needed)
# else need a new room

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        pq = list()
        rooms = 0
        for interval in sorted(intervals, key=lambda i: i.start):
            if pq and pq[0] <= interval.start:
                heapq.heapreplace(pq, interval.end)
            else:
                heapq.heappush(pq, interval.end)
                rooms += 1

        return rooms

# LUP solution
# Very similar with what we do in real life. Whenever you want to start a meeting,
# you go and check if any empty room available (available > 0) and
# if so take one of them ( available -=1 ). Otherwise,
# you need to find a new room someplace else ( numRooms += 1 ).
# After you finish the meeting, the room becomes available again ( available += 1 ).

class Solution(object):
    def minMeetingRooms(self, intervals):
        start, end = list(), list()
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort(reverse=True)
        rooms, available = 0, 0
        for i in range(len(start)):
            if end[-1] <= start[i]:
                end.pop()
                available += 1

            if not available:
                rooms += 1

            else:
                available -= 1

        return rooms