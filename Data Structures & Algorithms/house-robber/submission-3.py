class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = {}

        def dfs(i):
            if i >= N:
                return 0
            if i in memo:
                return memo[i]
            
            res = max(nums[i] + dfs(i + 2), dfs(i + 1))
            memo[i] = res
            return res
        
        return dfs(0)