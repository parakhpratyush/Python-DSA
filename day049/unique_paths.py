class Solution(object):
    def uniquePaths(self, m, n):
        # dp[i][j] = kitne unique paths hain (0,0) se (i,j) tak
        dp = [[1] * n for _ in range(m)]
        
        # First row aur first col = sirf 1 tarika (straight line)
        # Baaki cells = upar se + left se
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

#----Testing----
solver = Solution()
print(solver.uniquePaths(3, 7))   # 28
print(solver.uniquePaths(3, 2))   # 3
print(solver.uniquePaths(1, 1))   # 1