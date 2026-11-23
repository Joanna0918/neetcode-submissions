class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in numsSet: # find the beginning of the array
                num = n
                cnt = 0
                while num in numsSet:
                    cnt += 1
                    num += 1
                res = max(res, cnt)

        return res