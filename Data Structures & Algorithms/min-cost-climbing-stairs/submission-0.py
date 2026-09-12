class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            print('test')
            return min(cost)

        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            print('i', i)
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
            print('cost[i]', cost[i])
        
        return min(cost[0], cost[1])