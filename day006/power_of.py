#for power of 2
class Solution(object):
    def isPowerOfTwo(n):
        for i in range(50):
            if n==(2**i):
                return True
        return False

print(Solution.isPowerOfTwo(64))
print(Solution.isPowerOfTwo(54))

#for power of 3
class Solution(object):
    def isPowerOfThree(n):
        for i in range(50):
            if n==(3**i):
                return True
        return False
    
print(Solution.isPowerOfThree(81))
print(Solution.isPowerOfThree(63))

#for power of 4
class Solution(object):
    def isPowerOfFour(n):
        for i in range(50):
            if n==(4**i):
                return True
        return False
    
print(Solution.isPowerOfFour(256))
print(Solution.isPowerOfFour(745))