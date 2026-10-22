class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preSum = 1
        prefix = []
        for n in nums:
            prefix.append(preSum)
            preSum *= n
        
        sufSum = 1
        suffix = []
        for n in nums[::-1]:
            suffix.append(sufSum)
            sufSum *= n

        return [x * y for x, y in zip(prefix, suffix[::-1])]