class Solution(object):
    def isHappy(n):
        if n==1:
            return True
        f_n=0
        rev = 0
        seen = set()
        seen.add(n)
        while f_n != 1:
            rem = n % 10
            rev = rev + (rem ** 2)
            n = n // 10
            if n == 0:
                f_n = rev
                if f_n in seen:
                    return False
                seen.add(f_n)
                n = rev
                rev = 0
                
        return f_n == 1
    
print(Solution.isHappy(19))
print(Solution.isHappy(7))
print(Solution.isHappy(1))
print(Solution.isHappy(2))
        