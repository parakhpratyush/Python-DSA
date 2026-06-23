from collections import Counter
class Solution():
    def minWindow(self,s, t):
        if not t or not s:
            return ""
    
        need = Counter(t)
        missing = len(t)
        left = 0
        result = (0, float('inf'))
    
        for right, char in enumerate(s):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
        
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
            
                if right - left < result[1] - result[0]:
                    result = (left, right)
            
                need[s[left]] += 1
                missing += 1
                left += 1
    
        return s[result[0]:result[1]+1] if result[1] < float('inf') else ""
    
#----Testing----
solver=Solution()

print(solver.minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(solver.minWindow(s = "a", t = "a"))
print(solver.minWindow(s = "a", t = "aa"))