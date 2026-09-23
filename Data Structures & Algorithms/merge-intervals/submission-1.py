class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for interval in intervals:
            latestEnd = res[-1][1]

            if interval[0] <= latestEnd:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        
        return res