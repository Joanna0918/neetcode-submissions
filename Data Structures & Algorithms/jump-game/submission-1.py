class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        
        def dfs(i):
            if i >= len(nums) - 1:
                return True
            if i in dp:
                return dp[i]
            
            for step in range(1, nums[i] + 1):
                if dfs(i + step):
                    dp[i] = True
                    return True
            dp[i] = False
            return False

        return dfs(0)