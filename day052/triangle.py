class Solution(object):
    def minimumTotal(self, triangle):
        # Bottom-up DP
        # Neeche se upar aao
        dp = triangle[-1][:]  # Last row copy karo
        
        # Neeche se upar traverse karo
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Current cell + min of two children below
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        
        return dp[0]

#----Testing----
solver = Solution()
print(solver.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))  # 11
print(solver.minimumTotal([[-10]]))                         # -10
