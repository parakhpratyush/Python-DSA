class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        n = len(passingFees)
        # dp[t][i] = min cost to reach city i in exactly t minutes
        INF = float('inf')
        dp = [[INF] * n for _ in range(maxTime + 1)]
        dp[0][0] = passingFees[0]
        
        for t in range(1, maxTime + 1):
            for u, v, time in edges:
                if time <= t:
                    if dp[t-time][u] != INF:
                        dp[t][v] = min(dp[t][v], dp[t-time][u] + passingFees[v])
                    if dp[t-time][v] != INF:
                        dp[t][u] = min(dp[t][u], dp[t-time][v] + passingFees[u])
        
        ans = min(dp[t][n-1] for t in range(1, maxTime + 1))
        return ans if ans != INF else -1

#----Testing----
solver = Solution()
print(solver.minCost(30, [[0,1,10],[1,2,10],[2,5,10],[0,3,1],
                           [3,4,10],[4,5,15]], [5,1,2,20,20,3]))  # 11
print(solver.minCost(29, [[0,1,10],[1,2,10],[2,5,10],[0,3,1],
                           [3,4,10],[4,5,15]], [5,1,2,20,20,3]))  # -1