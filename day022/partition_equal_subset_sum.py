class Solution(object):
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
    
    
        dp = [False] * (target + 1)
        dp[0] = True # Base case: 0 sum hamesha possible hai
    
        for num in nums:

            for w in range(target, num - 1, -1):
                dp[w] = dp[w] or dp[w - num]
            
        return dp[target]

#Testing
solver=Solution() 

print(solver.canPartition([1,5,11,5]))
print(solver.canPartition([1,2,3,5]))