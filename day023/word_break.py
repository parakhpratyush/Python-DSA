class Solution():
    def wordBreak(self,s, wordDict):
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
    
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]

#Testing
solver=Solution()

print(solver.wordBreak("leetcode", ["leet","code"]))        
print(solver.wordBreak("applepenapple", ["apple","pen"]))   
print(solver.wordBreak("catsandog", ["cats","dog","sand","and","cat"])) 