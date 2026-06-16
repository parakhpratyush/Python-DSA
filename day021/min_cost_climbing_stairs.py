class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[n]

solver=Solution()    
print(solver.minCostClimbingStairs([10,15,20]))
print(solver.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))