class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []

        for s, e in intervals:
            if not res:
                res.append([s, e])
                continue
            
            prev_s, prev_e = res[-1]
            if prev_s <= s < prev_e:
                if prev_e <= e:
                    continue
                else:
                    res.pop()
                    res.append([s, e])
            else:
                res.append([s, e])
        
        return len(intervals) - len(res)