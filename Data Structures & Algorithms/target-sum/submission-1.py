class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def dfs(i, amount):
            if i == len(nums) and amount == target:
                return 1
            if i == len(nums) and amount != target:
                return 0

            if (i, amount) in dp:
                return dp[(i, amount)]
            
            dp[(i, amount)] = dfs(i + 1, amount + nums[i]) + dfs(i + 1, amount - nums[i])
            return dp[(i, amount)]
        
        return dfs(0, 0)