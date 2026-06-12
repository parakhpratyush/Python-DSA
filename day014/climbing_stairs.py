#Method 1
class Solution():
    def climbStairs(self,n):
        if n <= 2: return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

solver=Solution()   
print(solver.climbStairs(2))
print(solver.climbStairs(3))

#Method 2
class Solution():
    def climbStairs(self,n, memo={}):
        if n <= 2: return n
        if n in memo: return memo[n]
        memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        return memo[n]

solver=Solution()
print(solver.climbStairs(2))
print(solver.climbStairs(3))
