class Solution():
    def longestPrefix(self,s):
        lps = self.build_lps(s)
        return s[:lps[-1]]
    
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
    
#-----Testing-----
solver = Solution()
print(solver.longestPrefix("level"))
print(solver.longestPrefix("ababab"))