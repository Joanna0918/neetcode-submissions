class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set(nums)
        res = 1

        for n in numSet:
            if n-1 not in numSet:
                streak = 1
                while n + streak in numSet:
                    streak += 1
                res = max(res, streak)
        
        return res