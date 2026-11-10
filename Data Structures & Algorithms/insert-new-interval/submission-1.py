class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        insert = False
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res = res + intervals[i:]
                insert = True
                break
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        if not insert:
            res.append(newInterval)
        return res