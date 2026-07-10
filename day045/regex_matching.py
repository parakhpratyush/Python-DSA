class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        # dp[i][j] = kya s[:i] aur p[:j] match karte hain
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        
        # Empty string ke saath pattern match karne ke liye
        # 'a*', 'a*b*' jaisi patterns empty string se match kar sakti hain
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    # Zero occurrences: p[j-2] ko ignore karo
                    dp[i][j] = dp[i][j-2]
                    # One or more: agar p[j-2] current char se match karta hai
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                elif p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
        
        return dp[m][n]


#----Testing----
solver = Solution()
print(solver.isMatch("aa", "a"))      # False
print(solver.isMatch("aa", "a*"))     # True
print(solver.isMatch("ab", ".*"))     # True
print(solver.isMatch("aab", "c*a*b")) # True