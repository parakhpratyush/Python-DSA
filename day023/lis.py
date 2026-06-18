class Solution():
    def lengthOfLIS(self,nums):
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

#Testing
solver=Solution()

print(solver.lengthOfLIS([10,9,2,5,3,7,101,18])) 
print(solver.lengthOfLIS([0,1,0,3,2,3]))         
print(solver.lengthOfLIS([7,7,7,7]))              