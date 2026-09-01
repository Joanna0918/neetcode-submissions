class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            time = self.hasEaten(piles, m, h)
            if time == -1:
                l = m + 1
            else:
                res = min(res, m)
                r = m - 1
        
        return res
        
    
    def hasEaten(self, piles, k, target):
        hours = 0

        for b in piles:
            hours += math.ceil(b / k)
        
        if hours > target:
            return -1
        else:
            return 1