class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        nums = [0] + nums

        for i in range(3, n + 1):
            nums[i] = max(nums[i] + nums[i-2], nums[i] + nums[i-3])
        
        return max(nums[n], nums[n-1])