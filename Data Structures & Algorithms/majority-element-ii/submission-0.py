class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        res = set()

        for n in nums:
            count[n] += 1
            if count[n] > len(nums) / 3:
                res.add(n)
        
        return list(res)