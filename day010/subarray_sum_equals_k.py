class Solution(object):
    def subarraysum(nums,k):
        from collections import defaultdict
        count = 0
        curr_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1 
        for num in nums:
            curr_sum += num
            count += prefix_counts[curr_sum - k]
            prefix_counts[curr_sum] += 1
        return count 



print(Solution.subarraysum([100,1,2,3,100,1,2,3,4],3))
