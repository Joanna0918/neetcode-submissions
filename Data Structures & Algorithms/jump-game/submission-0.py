class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        distance = 1

        while goal >= 0 and goal - distance >= 0:
            
            if nums[goal - distance] >= distance: # can reach goal from [goal - distance]
                goal = goal - distance
                distance = 1
            else:
                distance += 1
        
        return goal == 0