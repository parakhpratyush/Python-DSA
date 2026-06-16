import time

class DPEngine:
    """
    Subsystem designed to demonstrate the transition from exponential recursive structures
    to optimized linear time complexity using Top-Down and Bottom-Up DP methodologies.
    """
    
    def fib_brute_force(self, n: int) -> int:
        """Time Complexity: O(2^N) - Exponential Explosion"""
        if n <= 1:
            return n
        return self.fib_brute_force(n - 1) + self.fib_brute_force(n - 2)

    def fib_memoization(self, n: int, memo: dict = None) -> int:
        """Time Complexity: O(N) | Space Complexity: O(N) Call Stack + Map"""
        if memo is None:
            memo = {}
        if n <= 1:
            return n
        if n in memo:
            return memo[n]  # Return pre-computed state instantly
            
        memo[n] = self.fib_memoization(n - 1, memo) + self.fib_memoization(n - 2, memo)
        return memo[n]

    def fib_tabulation(self, n: int) -> int:
        """Time Complexity: O(N) | Space Complexity: O(N) - No call stack overhead"""
        if n <= 1:
            return n
        
        # Initialize DP Table
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        # Iterative State Transition
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[n]

    def fib_space_optimized(self, n: int) -> int:
        """Time Complexity: O(N) | Space Complexity: O(1) - Ultimate System Optimization"""
        if n <= 1:
            return n
        
        prev2 = 0  # Represents dp[i-2]
        prev1 = 1  # Represents dp[i-1]
        
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
            
        return prev1

# =====================================================================
# PIPELINE EXECUTION & PROFILE AUDIT
# =====================================================================
if __name__ == "__main__":
    engine = DPEngine()
    target_state = 35  # Higher numbers will freeze brute force completely
    
    print("--- ⚔️ Day 21: Executing DP Optimization Benchmarks ---")
    
    # 1. Memoization Pipeline
    start = time.time()
    memo_res = engine.fib_memoization(target_state)
    print(f"[MEMOIZATION] Result: {memo_res} | Runtime: {(time.time() - start):.6f}s")
    
    # 2. Tabulation Pipeline
    start = time.time()
    tab_res = engine.fib_tabulation(target_state)
    print(f"[TABULATION]  Result: {tab_res} | Runtime: {(time.time() - start):.6f}s")
    
    # 3. Space Optimized Pipeline
    start = time.time()
    opt_res = engine.fib_space_optimized(target_state)
    print(f"[SPACE OPT]   Result: {opt_res} | Runtime: {(time.time() - start):.6f}s")