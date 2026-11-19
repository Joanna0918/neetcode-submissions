"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        prev_end = 0

        for i in range(len(intervals)):
            if intervals[i].start < prev_end:
                return False
            else:
                prev_end = intervals[i].end
        
        return True