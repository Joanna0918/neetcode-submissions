class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2

            cnt = 0
            for p in piles:
                cnt += (p + k - 1) // k
            
            if cnt <= h:
                res = min(res, k)
                r = k - 1
            elif cnt > h:
                l = k + 1
        
        return res