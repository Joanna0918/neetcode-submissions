class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        res = 0
        prefix = 0

        for n in nums:
            prefix += n
            subtract = prefix - k
            if subtract in prefixSum:
                res += prefixSum[subtract]
            prefixSum[prefix] = prefixSum.get(prefix, 0) + 1
        
        return res