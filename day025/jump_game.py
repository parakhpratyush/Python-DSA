class Solution():
    def canJump(self,nums):
        max_reach = 0
    
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True

solver=Solution()

print(solver.canJump([2,3,1,1,4]))
print(solver.canJump([3,2,1,0,4]))
print(solver.canJump([0]))