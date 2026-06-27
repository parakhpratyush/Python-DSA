class Solution():
    def countPrimes(self,n):
        if n < 2:
            return 0
    
        is_prime = [True] * n
        is_prime[0] = False
        if n > 1:
            is_prime[1] = False if n > 1 else None
    
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
    
        return sum(is_prime)
    
#----Testing----
solver=Solution()

print(solver.countPrimes(10))
print(solver.countPrimes(0))
print(solver.countPrimes(1))

