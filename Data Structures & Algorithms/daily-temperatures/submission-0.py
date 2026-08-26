class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if not tempStack:
                tempStack.append((i, t))
            
            prev_temp = tempStack[-1][1]
            while t > prev_temp:
                prev = tempStack.pop()
                res[prev[0]] = i - prev[0]

                if tempStack:
                    prev_temp = tempStack[-1][1]
                else:
                    break
            
            tempStack.append((i, t))
        
        return res