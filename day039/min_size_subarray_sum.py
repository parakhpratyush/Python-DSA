class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        current_sum = 0
        min_len = float('inf')
        
        for right in range(len(nums)):
            # Window expand karo — right element add karo
            current_sum += nums[right]
            
            # Jab tak condition satisfy hai — window contract karo
            # Kyun? Hum minimum length chahte hain
            # Toh jab sum >= target ho, left ko aage badho
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return min_len if min_len != float('inf') else 0

#----Testing----
solver = Solution()
print(solver.minSubArrayLen(7, [2,3,1,2,4,3]))   # 2 ([4,3])
print(solver.minSubArrayLen(4, [1,4,4]))           # 1 ([4])
print(solver.minSubArrayLen(11, [1,1,1,1,1,1,1])) # 0 (impossible)