class Solution(object):
    def permute(nums):
        result = []
    
        def backtrack(current, remaining):
            if not remaining:
                result.append(current[:])
                return
            for i in range(len(remaining)):
                current.append(remaining[i])
                backtrack(current, remaining[:i] + remaining[i+1:])
                current.pop()
    
        backtrack([], nums)
        return result

print(Solution.permute([1,2,3]))
print(Solution.permute([0,1]))
print(Solution.permute([1]))