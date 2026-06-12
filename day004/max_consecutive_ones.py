class Solution(object):
    def findMaxConsecutiveOnes(nums):
        maxi=0
        curr=0
        for i in nums:
            if i==1:
                curr+=i
                maxi=max(curr,maxi)
            else:
                curr=0
        return max(curr,maxi)


print(Solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(Solution.findMaxConsecutiveOnes([1,0,1,1,0,1]))