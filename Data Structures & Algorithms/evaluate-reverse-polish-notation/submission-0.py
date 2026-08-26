class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        operators = {'+', '-', '*', '/'}

        for n in tokens:
            if n not in operators:
                numStack.append(int(n))
            else:
                num1 = numStack.pop()
                num2 = numStack.pop()
                if n == '+':
                    newNum = num2 + num1
                elif n == '-':
                    newNum = num2 - num1
                elif n == '*':
                    newNum = num2 * num1
                else:
                    newNum = int(num2 / num1)
                
                numStack.append(newNum)
        
        return numStack.pop()