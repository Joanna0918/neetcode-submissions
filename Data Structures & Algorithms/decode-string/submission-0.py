class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                cur = ""
                while stack:
                    prev = stack.pop()
                    if prev == "[":
                        break
                    cur = prev + cur

                # get integer
                mul = ""
                while stack:
                    if stack[-1] not in "0123456789":
                        break
                    mul = stack.pop() + mul

                cur = int(mul) * cur
                stack.append(cur)
            else:
                stack.append(c)
        
        return "".join(stack)