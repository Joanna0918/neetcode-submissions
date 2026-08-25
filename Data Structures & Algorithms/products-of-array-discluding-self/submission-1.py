class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt, prod = 0, 1
        l = len(nums)
        res = [0] * l
        
        for n in nums:
            if n == 0:
                zero_cnt += 1
            else:
                prod *= n

        if zero_cnt > 1:
            return [0] * l
        
        for i, n in enumerate(nums):
            if zero_cnt == 1 and n != 0:
                res[i] = 0
            elif zero_cnt == 1 and n == 0:
                res[i] = int(prod)
            else:
                res[i] = int(prod / n)

        return res