class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res, curSum = len(nums) + 1, nums[0]

        while l <= r and r < len(nums):
            if curSum >= target:
                res = min(res, r - l + 1)
                curSum -= nums[l]
                l += 1
            else:
                r += 1
                if r < len(nums):
                    curSum += nums[r]
        return res if res != len(nums) + 1 else 0