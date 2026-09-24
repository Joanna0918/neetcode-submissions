class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        nums_0 = [0] * count[0]
        nums_1 = [1] * count[1]
        nums_2 = [2] * count[2]

        nums[:] = (
            [0] * count[0]
            + [1] * count[1]
            + [2] * count[2]
        )
