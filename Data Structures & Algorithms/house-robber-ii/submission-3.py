class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        N = len(nums)
        memo = [ [-1] * 2 for _ in range(N) ]

        def dfs(i, flag):
            if i >= N or (flag and i == len(nums) - 1):
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            
            res = max(nums[i] + dfs(i + 2, flag or i == 0), dfs(i + 1, flag))
            memo[i][flag] = res
            return res
        
        return max(dfs(0, True), dfs(1, False))