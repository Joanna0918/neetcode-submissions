class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(selected, cursum, i):
            if cursum == target:
                res.append(list(selected))
                return
            
            for j in range(i, len(nums)):
                n = nums[j]
                if cursum + n <= target:
                    # Pass j instead of j + 1 to allow reusing the same element
                    dfs(selected + [n], cursum + n, j)
                    
        dfs([], 0, 0)
        return res