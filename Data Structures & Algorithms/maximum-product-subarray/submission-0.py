class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minimum, maximum = nums[0], nums[0]

        for n in nums[1:]:
            prev_min = minimum
            prev_max = maximum

            minimum = min(n, n * prev_min, n * prev_max)
            maximum = max(n, n * prev_min, n * prev_max)
            res = max(res, maximum)
        
        return res