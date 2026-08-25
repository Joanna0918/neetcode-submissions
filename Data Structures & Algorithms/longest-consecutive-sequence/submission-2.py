class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = list(sorted(set(nums)))
        res = 1
        streak = 1
        curr = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == curr+1:
                streak += 1
            else:
                streak = 1
            
            curr = nums[i]
            res = max(res, streak)
        
        return res