class Solution():
    def countSubstrings(self,s):
        count = 0
    
        def expand(left, right):
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
    
        for i in range(len(s)):
            expand(i, i)      
            expand(i, i+1)   
    
        return count

#----Testing----

solver=Solution()

print(solver.countSubstrings("abc"))
print(solver.countSubstrings("aaa"))

#('---------------------------------------------------------------------OR----------------------------------------------------------------------------------')
class Solution(object):
    def countSubstrings(self, s):
        self.count = 0 
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.count += 1
                left -= 1
                right += 1
                
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
            
        return self.count
    
solver=Solution()

print(solver.countSubstrings("abcde"))
print(solver.countSubstrings("aaaaa"))
