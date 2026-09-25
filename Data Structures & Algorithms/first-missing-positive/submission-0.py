class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = set(nums)
        n = 1
        
        for _ in range(len(nums)):
            if n in numSet:
                n += 1
            else:
                break
        
        return n