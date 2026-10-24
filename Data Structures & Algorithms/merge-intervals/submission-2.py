class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for start, end in intervals:
            if not res:
                res.append([start, end])
                continue
            prev_s, prev_e = res[-1]
            if prev_e < start:
                res.append([start, end])
            else:
                res.pop()
                new_e = max(end, prev_e)
                res.append([prev_s, new_e])

        return res