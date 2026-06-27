class Solution():
    def myPow(self,x, n):
        if n < 0:
            x = 1 / x
            n = -n
    
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
    
        return result

#----Testing----
solver=Solution()

print(solver.myPow(x = 2.00000, n = 10))
print(solver.myPow(x = 2.10000, n = 3))
print(solver.myPow(x = 2.00000, n = -2))