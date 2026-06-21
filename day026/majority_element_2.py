class Solution(object):
    def majorityElement(self, nums):
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
    
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
    
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums) // 3:
                result.append(c)
    
        return result

#Testing

solver=Solution()

print(solver.majorityElement([3,2,3]))     
print(solver.majorityElement([1,1,1,3,3,2,2,2])) 