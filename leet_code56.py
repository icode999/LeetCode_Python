"""
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

Hide Company Tags LinkedIn Google Facebook Twitter Microsoft Bloomberg Yelp
Show Tags
Show Similar Problems

"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda i:i.start)
        result = list()
        if intervals:
            start = intervals[0]
            for end in intervals[1:]:
                if start.start <= end.start and start.end >= end.start:
                    if start.end <= end.end:
                        start.end = end.end
                else:
                    result.append(start)
                    start = end

            result.append(start)
        return result