class Solution():
    def strStr(self,haystack, needle):
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
    
        lps = self.build_lps(needle)
        i = j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
    
        return -1

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

solver = Solution()

print(solver.strStr("leetcode", needle = "leeto"))
print(solver.strStr(haystack = "sadbutsad", needle = "sad"))