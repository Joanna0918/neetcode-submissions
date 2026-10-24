class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [temperature, i]
        
        for i in range(len(temperatures)):            
            while stack and temperatures[i] > stack[-1][0]:
                temp, j = stack.pop()
                res[j] = i - j
            stack.append([temperatures[i], i])
        
        return res