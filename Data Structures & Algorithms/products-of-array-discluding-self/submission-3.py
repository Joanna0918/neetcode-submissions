class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        totalProducts = 1
        for n in nums:
            if n == 0:
                zeroCount += 1
            else:
                totalProducts *= n
        
        if zeroCount > 1:
            return [0] * len(nums)
        
        res = []
        for n in nums:
            if zeroCount == 1:
                if n == 0:
                    res.append(int(totalProducts))
                else:
                    res.append(0)
            else:
                res.append(int(totalProducts / n))
        return res