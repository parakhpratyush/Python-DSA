# this works well but get TlE(TIME LIMIT EXCEEDS)
class Solution(object):
    def maxSubArray(nums):
        max_sum=nums[0]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sum=0
                for k in range(i,j+1):
                    sum+=nums[k]
                    if sum>max_sum:
                        max_sum=sum   

        return max_sum

# NEW CODE FOR MAXIMUM SUBAARAY WITHOUT TLE
class Solution(object):
    def maxSubArray(nums):
        max_sum=nums[0]
        curr_sum=nums[0]
        for i in range(1,len(nums)):
            curr_sum=max(nums[i],curr_sum + nums[i])
            max_sum=max(max_sum,curr_sum)

        return max_sum

        
print(Solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution.maxSubArray([5,4,-1,7,8]))
print(Solution.maxSubArray([1]))
print(Solution.maxSubArray([-1]))