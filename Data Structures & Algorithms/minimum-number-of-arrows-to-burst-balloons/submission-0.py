class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = []
        for x1, x2 in points:
            if not res:
                res.append([x1, x2])
                continue
            
            prev_x1, prev_x2 = res[-1]
            if x1 > prev_x2:
                res.append([x1, x2])
            else:
                res.pop()
                res.append([max(prev_x1, x1), min(prev_x2, x2)])
        return len(res)