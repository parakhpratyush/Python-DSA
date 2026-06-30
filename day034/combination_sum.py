class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
    
        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            if remaining < 0:
                return
        
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()

        backtrack(0, [], target)
        return result

#----Testing----
solver=Solution()

print(solver.combinationSum(candidates = [2,3,6,7], target = 7))
print(solver.combinationSum(candidates = [2,3,5], target = 8))