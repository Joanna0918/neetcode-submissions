class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_num = {nums[0]: 0}

        for i in range(1, len(nums)):
            require_first_num = target - nums[i]
            if require_first_num in first_num:
                return [first_num[require_first_num], i]
            else:
                first_num[nums[i]] = i
