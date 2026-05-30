class Solution(object):
    def containsDuplicate( nums):
        return len(nums)!=len(set(nums))

print(Solution.containsDuplicate([1,2,3,1]))  #--> True
print(Solution.containsDuplicate([1,2,3,4]))  #--> False