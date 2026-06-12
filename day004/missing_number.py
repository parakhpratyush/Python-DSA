#Given an array nums[] of size n with distinct integers in the range of [0, n].
class Solution(object):
    def missingNumber(nums):
        for n in range(0,len(nums)+1):
            if n not in nums:
                return n
            
print(Solution.missingNumber([3,0,1]))
print(Solution.missingNumber([0,1]))
print(Solution.missingNumber([8,6,4,2,3,5,7,0,1]))



#Given an array arr[] of size n-1 with distinct integers in the range of [1, n].
class Solu(object):
    def missingNumbers(arr):
        for n in range(1,len(arr)+1):
            if n not in arr:
                return n



print(Solu.missingNumbers([8, 2, 4, 5, 3, 7, 1]))
print(Solu.missingNumbers([1, 2, 3, 5]))

#method with time complexity O(N)
class Soln(object):
    def missing_Number(num):
        n=len(num)
        exp=n*(n+1)//2
        return exp-sum(num)
    
print(Soln.missing_Number([3,0,1]))
print(Soln.missing_Number([0,1]))
print(Soln.missing_Number([8,6,4,2,3,5,7,0,1]))