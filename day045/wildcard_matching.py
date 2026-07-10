class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        
        # '*' empty string se match kar sakta hai
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    # '*' ko zero characters se match karo: dp[i][j-1]
                    # '*' ko ek ya zyada se match karo: dp[i-1][j]
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
        
        return dp[m][n]



#----Testing----
solver = Solution()
print(solver.isMatch("aa", "a"))     # False
print(solver.isMatch("aa", "*"))     # True
print(solver.isMatch("cb", "?a"))    # False
print(solver.isMatch("adceb", "*a*b")) # True

