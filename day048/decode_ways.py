class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # empty string
        dp[1] = 1  # first character (already checked not '0')
        
        for i in range(2, n + 1):
            # Single digit decode
            one_digit = int(s[i-1])
            if one_digit >= 1:
                dp[i] += dp[i-1]
            
            # Two digit decode
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]

#----Testing----
solver = Solution()
print(solver.numDecodings("12"))    # 2 ("AB" or "L")
print(solver.numDecodings("226"))   # 3
print(solver.numDecodings("06"))    # 0 (invalid)
print(solver.numDecodings("11106")) # 2