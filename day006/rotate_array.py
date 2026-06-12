class Solution(object):
    def rotate(nums, k):
        n = len(nums)
        if n == 0 or n == 1:
            return nums
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
        return nums[:-k]

print(Solution.rotate([1,8,3,4,5,6],3))




