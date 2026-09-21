class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) - 1
        if n == 0:
            return 0
        step = [len(nums)] * len(nums)

        for i in range(n - 1, -1, -1):
            if n - i <= nums[i]:
                step[i] = 1
            
            else:
                for j in range(i, i + nums[i] + 1):
                    step[i] = min(step[i], step[j])
                step[i] += 1
        
        return step[0]