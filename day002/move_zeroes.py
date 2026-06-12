class Solution(object):
    def moveZeroes( nums):
        temp=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                temp.append(nums[i])
        for i in range(len(temp)):
            nums[i]=temp[i]
            no_nz=len(temp)
            for i in range(no_nz,len(nums)):
                nums[i]=0
        return(nums)



print(Solution.moveZeroes([0,1,0,3,12]))