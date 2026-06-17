def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            item_weight = weights[i - 1]
            item_value = values[i - 1]
            if item_weight > w:
                dp[i][w] = dp[i-1][w]
            
            else:
                dp[i][w] = max(dp[i-1][w],item_value + dp[i-1][w - item_weight])
    return dp[n][W]


# Test
weights = [1, 3, 4, 5]
values  = [1, 4, 5, 7]
W = 7

print("Max value:", knapsack(weights, values, W))  # 9