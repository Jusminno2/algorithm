from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost))]

        for i in range(len(cost)):
            if i == 0:
                dp[i] = cost[i]
            elif i == 1:
                dp[i] = min(dp[i - 1] + cost[i], cost[i])
            else:
                dp[i] = min(dp[i - 2] + cost[i], dp[i - 1] + cost[i])

        return min(dp[len(cost) - 1], dp[len(cost) - 2])
