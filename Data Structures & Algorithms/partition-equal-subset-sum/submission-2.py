class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2
        memo = {}
        
        def dfs(i, curSum):
            if i == len(nums):
                return False
            if curSum == target:
                return True
            if (i, curSum) in memo:
                return  memo[(i, curSum)]

            if (dfs(i + 1, curSum)
                or dfs(i + 1, curSum + nums[i])):
                memo[(i, curSum)] = True
                return True
            else:
                memo[(i, curSum)] = False
                return False
        
        return dfs(0, 0)