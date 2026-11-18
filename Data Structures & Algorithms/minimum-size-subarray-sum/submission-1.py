class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        resSum = 0
        res = len(nums) + 1
        for r in range(len(nums)):
            resSum += nums[r]
            while resSum >= target:
                if (r - l) + 1 < res:
                    res = (r - l) + 1
                resSum -= nums[l]
                l += 1
        return res if res < len(nums) + 1 else 0