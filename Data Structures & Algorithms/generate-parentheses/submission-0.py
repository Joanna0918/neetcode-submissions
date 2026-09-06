class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        parentheses = ""
        open, close = 0, 0

        def backtrack(open, close, parentheses):
            if open > n or close > n or close > open:
                return
            if open == close == n:
                res.append(parentheses)
            
            # add "("
            parentheses += "("
            backtrack(open + 1, close, parentheses)

            # add ")"
            parentheses = parentheses[:-1]
            parentheses += ")"
            backtrack(open, close + 1, parentheses)
        
        backtrack(open, close, parentheses)
        return res