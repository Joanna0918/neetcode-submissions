class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = 0

        while l <= r:
            m = (l + r) // 2
            count, prev = 1, weights[0]
            for w in weights[1:]:
                if prev + w > m:
                    count += 1
                    prev = w
                else:
                    prev += w
            if count > days:
                l = m + 1
            else:
                res = m
                r = m - 1
        
        return res
        