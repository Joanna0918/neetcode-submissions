class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        cnt = [0] * (n + 1)
        cnt[n - 1] = 1
        cnt[n - 2] = 2

        for i in range(n - 3, -1, -1):
            cnt[i] = cnt[i + 1] + cnt[i + 2]
        
        return cnt[0]