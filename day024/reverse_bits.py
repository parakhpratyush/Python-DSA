class Solution():
    def reverseBits(self,n):
        result = 0
        for i in range(32):
            bit = n & 1
            result = (result << 1) | bit
            n >>= 1
    
        return result

#Testing
solver=Solution()

print(solver.reverseBits(0b00000010100101000001111010011100))
print(solver.reverseBits(0b01111111111111111111111111111100))