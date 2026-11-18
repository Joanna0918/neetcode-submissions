class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[-1] * len(prices) for _ in range(2)] # memo[r][c], r: ith day, c: T/F of canBuy

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0

            if memo[canBuy][i] != -1:
                return memo[canBuy][i]
            
            if canBuy:
                buy = dfs(i + 1, False) - prices[i]
                notBuy = dfs(i + 1, True)
                memo[canBuy][i] = max(buy, notBuy)
            else:
                sell = dfs(i + 2, True) + prices[i]
                notSell = dfs(i + 1, False)
                memo[canBuy][i] = max(sell, notSell)
            return memo[canBuy][i]
        
        return dfs(0, True)