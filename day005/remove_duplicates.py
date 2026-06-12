#In-Place Modification (Two-Pointer Approach)
class Solution(object):
    def removeDuplicates(nums):
        count=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[count]=nums[i]
                count+=1
        return count

print((Solution.removeDuplicates([1,1,2])))
print(Solution.removeDuplicates([0,0,1,1,1,2,2,2,4,5]))    


#Array Generation (Extra Space Approach)
class Solution(object):
    def removeDuplicates(nums):
        exp_nums=[nums[0]]
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                exp_nums.append(nums[i+1])
        nums[:] = exp_nums
        return nums
    
print(Solution.removeDuplicates([1,1,2]))
print(Solution.removeDuplicates([0,0,1,1,1,2,2,2,4,5]))
