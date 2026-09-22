class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        alreadyMerge = False
        for interval in intervals:
            if alreadyMerge:
                res.append(interval)
                continue
            
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                res.append(interval)
                alreadyMerge = True
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        
        if not alreadyMerge:
            res.append(newInterval)
        return res