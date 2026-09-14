class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) / 2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums)):
            for n in list(dp):
                dp.add(n + nums[i])
        
        return True if target in dp else False