class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def simple_rob(houses):
            prev2, prev1 = 0, 0
            for money in houses:
                curr = max(prev1, money + prev2)
                prev2 = prev1
                prev1 = curr
            return prev1
        return max(simple_rob(nums[:-1]), simple_rob(nums[1:]))
    
solver=Solution()

print(solver.rob([2,3,2]))
print(solver.rob([1,2,3,1]))
print(solver.rob([1,2,3]))