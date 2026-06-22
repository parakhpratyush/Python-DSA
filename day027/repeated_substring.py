class Solution():
    def repeatedSubstringPattern(self,s):
        n = len(s)
        lps = self.build_lps(s)
        length = lps[n - 1]
        return length > 0 and n % (n - length) == 0

    def build_lps(self,pattern):
        n = len(pattern)
        lps = [0] * n
        length = 0 
        i = 1
    
        while i < n:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
    
        return lps
    
#----Testing----

solver=Solution()

print(solver.repeatedSubstringPattern("abab"))
print(solver.repeatedSubstringPattern("aba"))
print(solver.repeatedSubstringPattern("abcabcabcabc"))