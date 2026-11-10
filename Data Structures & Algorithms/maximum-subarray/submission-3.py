class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        self.res = nums[0]
        
        def dfs(i, prev_sum):
            if i >= len(nums):
                return
            
            curr_sum = max(nums[i], prev_sum + nums[i])
            self.res = max(self.res, curr_sum)

            dfs(i + 1, curr_sum)
        
        dfs(1, nums[0])
        return self.res