# ==========================================
# FIBONACCI — TEEN APPROACHES
# ==========================================

# Approach 1: Pure Recursion (WRONG for large n)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Approach 2: Memoization (Top-Down DP)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Approach 3: Tabulation (Bottom-Up DP)
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Approach 4: Space Optimized
def fib_optimized(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1

# Test all approaches
print("Recursive fib(10):", fib_recursive(10))   # 55
print("Memo fib(50):", fib_memo(50))              # 12586269025
print("Tabulation fib(50):", fib_tab(50))         # 12586269025
print("Optimized fib(50):", fib_optimized(50))    # 12586269025

# Time it — see the difference
import time

start = time.time()
fib_recursive(35)
print(f"Recursive fib(35) time: {time.time()-start:.4f}s")

start = time.time()
fib_memo(35, {})
print(f"Memo fib(35) time: {time.time()-start:.6f}s")