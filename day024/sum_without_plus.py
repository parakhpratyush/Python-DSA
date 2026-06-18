class Solution(object):
    def getSum(self, a, b):
        mask = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = carry << 1 & mask
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)
    
        return a
    
#Testing
solver=Solution()

print(solver.getSum(1, 2))  
print(solver.getSum(-1, 1)) 
print(solver.getSum(3, 5))  