class Solution(object):
    def twoSum(nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

print(Solution.twoSum([7,2,11,14,15],9))
