class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        resMap = defaultdict(set)

        for i in range(len(nums)):
            if nums[i] not in resMap:
                num_i = nums[i]
                target_sum = -num_i

                l, r = i+1, len(nums)-1
                while l<r:
                    if nums[l] + nums[r] > target_sum:
                        r -= 1
                    elif nums[l] + nums[r] < target_sum:
                        l += 1
                    else:
                        resMap[num_i].add((nums[l], nums[r]))
                        r -= 1
                        l += 1
        
        res = []
        for i, pairs in resMap.items():
            for j, k in pairs:
                combination = [i, j, k]
                res.append(combination)
        
        return res