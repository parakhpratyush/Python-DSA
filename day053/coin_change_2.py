class Solution(object):
    def change(self, amount, coins):
        # dp[i] = kitne ways se amount i bana sakte hain
        dp = [0] * (amount + 1)
        dp[0] = 1  # 0 amount = 1 way (kuch mat lo)
        
        for coin in coins:
            for i in range(coin, amount + 1):
                # Is coin ko use karne se dp[i-coin] ways add ho jaate hain
                dp[i] += dp[i - coin]
        
        return dp[amount]

#----Testing----
solver = Solution()
print(solver.change(5, [1,2,5]))    # 4
print(solver.change(3, [2]))         # 0
print(solver.change(10, [10]))       # 1
