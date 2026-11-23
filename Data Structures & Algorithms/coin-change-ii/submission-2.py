class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, amt):
            if (i, amt) in memo:
                return memo[(i, amt)]
            if amt == 0:
                return 1
            if i == len(coins):
                return 0
            
            res = dfs(i + 1, amt)
            if amt - coins[i] >= 0:
                res += dfs(i, amt - coins[i])

            memo[((i, amt))] = res
            return res
        
        return dfs(0, amount)