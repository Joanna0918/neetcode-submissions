class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amt):
            if amt in memo:
                return memo[amt]
            if amt == 0:
                return 0
            if amt < 0:
                return float("inf")
            
            res = float("inf")
            for c in coins:
                res = min(res, 1 + dfs(amt - c))
            memo[amt] = res
            return res
        
        minC = dfs(amount)

        return minC if minC != float("inf") else -1