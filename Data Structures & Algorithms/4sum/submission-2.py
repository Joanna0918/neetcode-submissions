class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.res = []
        
        def nSum(i, n, subset, target):
            if len(nums) - i < n:
                return

            if n == 2:
                l, r = i, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] > target:
                        r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        self.res.append(subset + [nums[l], nums[r]])
                        l += 1
                        r -= 1

                        # Skip duplicates
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

            else:
                # select i
                nSum(i + 1, n - 1, subset + [nums[i]], target - nums[i])

                # not select i
                i += 1
                while i < len(nums) - 1 and nums[i] == nums[i - 1]:
                    i += 1
                nSum(i, n, subset, target)
        
        nSum(0, 4, [], target)
        return self.res