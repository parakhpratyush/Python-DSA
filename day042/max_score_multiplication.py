class Solution(object):
    def maximumScore(self, nums, multipliers):
        n = len(nums)
        m = len(multipliers)
        # dp[i][j] = max score after i operations, i-j from left, j from right
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                right = n - 1 - (i - left)
                mult = multipliers[i]
                dp[i][left] = max(
                    mult * nums[left] + dp[i+1][left+1],   # left se lo
                    mult * nums[right] + dp[i+1][left]      # right se lo
                )
        
        return dp[0][0]

#----Testing----
solver = Solution()
print(solver.maximumScore([1,2,3], [3,2,1]))              # 14
print(solver.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))  # 102