class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for interval in intervals:
            if not res:
                res.append(interval)
            
            else:
                prev_s, prev_e = res[-1][0], res[-1][1]
            
                if prev_s <= interval[0] <= prev_e:
                    res.pop()
                    res.append([prev_s, max(prev_e, interval[1])])
                else:
                    res.append(interval)
        return res