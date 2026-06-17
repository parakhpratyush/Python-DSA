class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
    
        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                
        return dp[amount] if dp[amount] != float('inf') else -1
    
#Testing
solver=Solution()

print(solver.coinChange(coins = [1,2,5], amount = 11))
print(solver.coinChange(coins = [2], amount = 3))
print(solver.coinChange(coins = [1], amount = 0))
