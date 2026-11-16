class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # create prefix and suffix max
        prefixMax, suffixMax = [0] * n, [0] * n
        prefixMax[0] = height[0]
        suffixMax[n - 1] = height[n - 1]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], height[i])
            suffixMax[n - i - 1] = max(suffixMax[n - i], height[n - i - 1])
        
        res = 0
        for i in range(1, n):
            if min(prefixMax[i], suffixMax[i]) >= height[i]:
                res += min(prefixMax[i], suffixMax[i]) - height[i]
        return res