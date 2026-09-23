class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0

        for interval in intervals[1:]:
            if interval[0] >= prevEnd: # no overlap
                prevEnd = interval[1]
            else:
                res += 1
                prevEnd = min(prevEnd, interval[1]) # remove the one with larger interval end
        return res