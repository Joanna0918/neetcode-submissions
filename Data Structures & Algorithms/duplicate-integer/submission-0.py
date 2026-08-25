class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        result = False
        for num in nums:
            if num in myMap:
                return True
            else:
                myMap[num] = 1
        return result
