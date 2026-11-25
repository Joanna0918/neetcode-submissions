class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i, j): # current index, prev selected index
            if i == len(nums):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            # not select current num
            res = dfs(i + 1, j)

            # select current num
            if j == -1 or nums[i] > nums[j]:
                res = max(1 + dfs(i + 1, i), res)
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, -1)