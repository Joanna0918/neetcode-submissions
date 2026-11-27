class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, curSum):
            if i == len(nums):
                return 0
            if curSum == target:
                return 1
            if (i, curSum) in memo:
                return memo[(i, curSum)]

            # not select nums[i]
            res = dfs(i + 1, curSum)
            
            # select nums[i]
            if curSum + nums[i] <= target:
                res += dfs(0, curSum + nums[i])
            
            memo[(i, curSum)] = res
            return res
        
        return dfs(0, 0)