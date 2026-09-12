class Solution:
    def rob_linear(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        nums = [0] + nums

        for i in range(3, n + 1):
            nums[i] = max(nums[i] + nums[i-2], nums[i] + nums[i-3])
        
        return max(nums[n], nums[n-1])


    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        return max(self.rob_linear(nums[1:]), self.rob_linear(nums[:len(nums)-1]))