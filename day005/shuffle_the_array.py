class Solution(object):
    def shuffle(nums, n):
        r_num=[]
        i=0
        j=n
        while i<n and j<(2*n):
            r_num.append(nums[i])
            r_num.append(nums[j])
            i+=1
            j+=1 
        nums[:]=r_num         
        return nums
    
print(Solution.shuffle([2,5,1,3,4,7],3))
print(Solution.shuffle([1,2,3,4,4,3,2,1],4))
print(Solution.shuffle([1,2,1,2],2))