class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []

        def dfs(i, subset):
            if i == len(nums):
                self.res.append(subset.copy())
                return
            
            # select current num
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            # not select current num
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            dfs(i, subset)
        
        dfs(0, [])
        return self.res