class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack, starStack = [], [] # both store index
        for i in range(len(s)):
            if s[i] == "(":
                leftStack.append(i)
            elif s[i] == "*":
                starStack.append(i)
            else: # s[i] == ")"
                if leftStack:
                    leftStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        
        while leftStack and starStack:
            l, s = leftStack.pop(), starStack.pop()
            if l > s:
                return False
        
        if leftStack and not starStack:
            return False
        
        return True