class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
        
        k = 0
        for i in range(len(nums)):
            if nums[i] == "_":
                j = i + 1
                while j < len(nums):
                    if nums[j] != "_":
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    else:
                        j += 1
                if j == len(nums):
                    return k
            
            k += 1
        return k