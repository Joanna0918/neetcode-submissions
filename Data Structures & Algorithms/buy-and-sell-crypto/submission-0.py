class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b, s = 0, 0

        while s <= (len(prices) - 1):
            buy, sell = prices[b], prices[s]
            profit = max(profit, sell - buy)
            if buy <= sell:
                s += 1
            else:
                b = s
                s += 1

        return profit