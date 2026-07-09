class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        best = 0
        
        for num in num_set:
            # Sirf sequence ka start check karo
            # num-1 nahi hona chahiye set mein
            if num - 1 not in num_set:
                current = num
                streak = 1
                
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                
                best = max(best, streak)
        
        return best


#----Testing----
solver = Solution()
print(solver.longestConsecutive([100,4,200,1,3,2]))   # 4 ([1,2,3,4])
print(solver.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # 9