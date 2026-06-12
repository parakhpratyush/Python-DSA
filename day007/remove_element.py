class Solution(object):
    def removeElement(nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)

print(Solution.removeElement([3,2,2,3],3))
print(Solution.removeElement([0,1,2,2,3,0,4,2],2))