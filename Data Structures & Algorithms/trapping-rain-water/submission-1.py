class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        rightMax = [0] * n
        leftMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])
        
        rightMax[n-1] = height[n-1]
        for j in range(n-1-1, 0, -1):
            rightMax[j] = max(rightMax[j+1], height[j])
        
        res = 0
        for index in range(n):
            trapArea = max(min(leftMax[index], rightMax[index]) - height[index], 0)
            res += trapArea
        
        return res