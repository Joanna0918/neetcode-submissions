class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        robMap = {}

        def dfs(i):
            if i >= n:
                return 0
            if i in robMap:
                return robMap[i]

            res = max(nums[i] + dfs(i + 2), dfs(i + 1))
            robMap[i] = res
            return res
        
        return dfs(0)