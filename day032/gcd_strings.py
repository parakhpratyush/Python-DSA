class Solution():
    def gcdOfStrings(self,str1, str2):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
    
        if str1 + str2 != str2 + str1:
            return ""
    
        g = gcd(len(str1), len(str2))
        return str1[:g]
    
#----Testing----
solver=Solution()

print(solver.gcdOfStrings(str1= "ABCABC", str2 = "ABC"))
print(solver.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
print(solver.gcdOfStrings(str1 = "LEET", str2 = "CODE"))
print(solver.gcdOfStrings(str1 = "AAAAAB", str2 = "AAA"))










