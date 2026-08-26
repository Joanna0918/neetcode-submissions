class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carMap = {}

        for i in range(len(position)):
            carMap[position[i]] = speed[i]
        
        carMap = dict(sorted(carMap.items(), reverse = True))
        timeStack = []

        for p, s in carMap.items():
            time = (target - p) / s

            if timeStack:
                if timeStack[-1] < time:
                    timeStack.append(time)
            else:
                timeStack.append(time)
        
        return len(timeStack)