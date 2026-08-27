class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights)-1
        while l < r:
            currArea = (r-l) * min(heights[l], heights[r])
            res = max(res, currArea)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                if heights[l+1] > heights[r-1]:
                    l += 1
                else:
                    r -= 1
        
        return res