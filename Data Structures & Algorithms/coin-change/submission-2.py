class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amountMap = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in amountMap:
                return amountMap[amount]
            
            res = float("inf")
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c))
            amountMap[amount] = res
            return res
        
        res = dfs(amount)
        return res if dfs(amount) < float("inf") else -1