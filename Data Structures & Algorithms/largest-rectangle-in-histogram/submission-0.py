class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            if not stack:
                stack.append((i, h))
            else:
                prev = stack[-1]
                new_index = i

                while prev[1] > h and stack:
                    area = (i - prev[0]) * prev[1]
                    res = max(res, area)
                    pop_item = stack.pop()
                    new_index = pop_item[0]
                    if stack:
                        prev = stack[-1]
                    else:
                        break
                
                stack.append((new_index, h))

        while stack:
            stack_pop_i, stack_pop_h = stack.pop()
            area = (len(heights) - stack_pop_i) * stack_pop_h
            res = max(res, area)

        return res