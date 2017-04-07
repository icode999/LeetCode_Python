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
        count = 0
        rooms = 0
        for interval in sorted(intervals, key=lambda i: i.start):
            if pq and pq[0] <= interval.start:
                heapq.heapreplace(pq, interval.end)
            else:
                heapq.heappush(pq, interval.end)
                rooms += 1

        return rooms
