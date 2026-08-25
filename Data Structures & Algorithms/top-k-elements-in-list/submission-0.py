class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resMap = {}

        for n in nums:
            resMap[n] = resMap.get(n, 0) + 1

        sorted_resMap = dict(
            sorted(resMap.items(), key=lambda x: x[1])
        )
        res = []

        for i in range(k):
            res.append(sorted_resMap.popitem()[0])
        
        return res
