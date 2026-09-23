"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        count, res = 0, 0

        i, j = 0, 0
        while i < len(start):
            if start[i] < end[j]:
                count += 1
                res = max(res, count)
                i += 1
            else:
                count -= 1
                j += 1
        return res