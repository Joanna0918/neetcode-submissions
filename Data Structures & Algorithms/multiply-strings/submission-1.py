class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = int(num1), int(num2)
        if num1 > num2:
            num1, num2 = num2, num1
        
        def helper(num1, num2):
            if num1 == 1:
                return num2
            if num1 == 0 or num2 == 0:
                return 0
            res = helper(num1 // 2, num2 + num2)
            return num2 + res if num1 % 2 else res

        return str(helper(num1, num2))