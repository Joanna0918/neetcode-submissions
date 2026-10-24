class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        intervals.sort()

        for s, e in intervals:
            
            if res:
                prev_s, prev_e = res[-1][0], res[-1][1]
                if s >= prev_e:
                    res.append([s, e])
                else:
                    if prev_e > e:
                        res.pop()
                        res.append([s, e])
            
            else:
                res.append([s, e])
        
        return len(intervals) - len(res)