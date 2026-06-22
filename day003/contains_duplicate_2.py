class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen_map = {}
        for j in range(len(nums)):
            current_num = nums[j]
            if current_num in seen_map:
                i = seen_map[current_num]
                if abs(i - j) <= k:
                    return True
            seen_map[current_num] = j
        
        return False
    
#----Testing----
solver=Solution()

print(solver.containsNearbyDuplicate([1,2,3,1,2,3],2))
print(solver.containsNearbyDuplicate([1,2,3,1],3)) 
print(solver.containsNearbyDuplicate([1,0,1,1],1))
                    