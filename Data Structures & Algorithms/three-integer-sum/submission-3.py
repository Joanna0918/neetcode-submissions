class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []

        while i < len(nums) - 2:
            num_i = nums[i]
            target = 0 - num_i
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < target:
                    while j < len(nums) - 1 and nums[j + 1] == nums[j]:
                        j += 1
                    j += 1
                elif nums[j] + nums[k] > target:
                    while k > 0 and nums[k - 1] == nums[k]:
                        k -= 1
                    k -= 1
                else:
                    res.append([num_i, nums[j], nums[k]])
                    while j < len(nums) - 1 and nums[j + 1] == nums[j]:
                        j += 1
                    j += 1
                    while k > 0 and nums[k - 1] == nums[k]:
                        k -= 1
                    k -= 1

            while i < len(nums) - 2 and nums[i + 1] == num_i:
                i += 1
            i += 1
        
        return res