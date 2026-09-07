class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }

        def backtrack(digits):
            if digits == "":
                return []
            if digits in digits_map:
                return digits_map[digits]
            
            combinations = backtrack(digits[1:])
            res = []
            for c in combinations:
                for character in digits_map[digits[0]]:
                    res.append(character + c)
            return res
        
        result = backtrack(digits)
        return result