from collections import Counter
class Solution():
    def findAnagrams(self,s, p):
        n, m = len(s), len(p)
        if m > n:
            return []
    
        p_count = Counter(p)
        window_count = Counter(s[:m])
    
        result = []
        if window_count == p_count:
            result.append(0)
    
        for i in range(m, n):
            window_count[s[i]] += 1
            window_count[s[i - m]] -= 1
            if window_count[s[i - m]] == 0:
                del window_count[s[i - m]]
        
            if window_count == p_count:
                result.append(i - m + 1)
    
        return result
    
#----Testing----
solver = Solution()

print(solver.findAnagrams(s = "cbaebabacd", p = "abc"))
print(solver.findAnagrams(s = "abab", p = "ab"))