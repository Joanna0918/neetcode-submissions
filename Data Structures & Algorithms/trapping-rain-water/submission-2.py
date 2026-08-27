class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        res = 0

        while l < r:
            if maxLeft < maxRight:
                trapArea = maxLeft - height[l]
                l += 1
                maxLeft = max(maxLeft, height[l])
            else:
                trapArea = maxRight - height[r]
                r -= 1
                maxRight = max(maxRight, height[r])
            
            res += max(trapArea, 0)
        
        return res
