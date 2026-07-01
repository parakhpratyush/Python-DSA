class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
    
        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return
        
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remaining:
                    break
            
                current.append(candidates[i])
                backtrack(i + 1, current, remaining - candidates[i])
                current.pop()
    
        backtrack(0, [], target)
        return result

#----Testing----
solver=Solution()

print(solver.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
print(solver.combinationSum2(candidates = [2,5,2,1,2], target = 5))