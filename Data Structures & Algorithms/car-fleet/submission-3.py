class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in posSpeed:
            t = (target - p) / s

            if not stack:
                stack.append(t)
            else:
                if t > stack[-1]: # start a new fleet
                    stack.append(t)
        
        return len(stack)