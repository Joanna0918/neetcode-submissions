class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins[::-1]:
            nextdp = [0] * (amount + 1)
            nextdp[0] = 1

            for i in range(1, amount + 1):
                if i - c >= 0:
                    nextdp[i] = nextdp[i - c] + dp[i]
            dp = nextdp
        
        return dp[amount]