class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        i = n - 2
        dp = [1, 1]
        while i > 0:
            tmp = dp[0]
            dp[0] = dp[0] + dp[1]
            dp[1] = tmp
            i -= 1
        return dp[0] + dp[1]