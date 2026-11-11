class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost
        n = len(cost)
        dp = [0] * n
        dp[n - 1], dp[n - 2] = cost[n - 1], cost[n - 2]

        for i in range(n - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i + 2], dp[i + 1])
        
        return dp[0]