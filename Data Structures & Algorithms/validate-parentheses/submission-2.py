class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        seen = []

        for p in s:
            if p == '(' or p == '[' or p == '{':
                seen.append(p)
            else:
                if seen and seen.pop() == match[p]:
                    continue
                else:
                    return False
        
        if seen:
            return False
        else:
            return True