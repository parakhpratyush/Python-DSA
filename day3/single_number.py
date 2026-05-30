class Solution(object):
    def singleNumber(nums):
        result=0
        for n in nums:
            result^=n

        return result
    
print(Solution.singleNumber([2,1,3,2,4,3,4]))