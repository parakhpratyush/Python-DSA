from collections import defaultdict

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        
        def at_most_k(k):
            # At most k distinct integers wale subarrays count karo
            count = defaultdict(int)
            left = 0
            result = 0
            
            for right in range(len(nums)):
                # Naya element add karo window mein
                count[nums[right]] += 1
                
                # Agar distinct > k, window contract karo
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                
                # right - left + 1 = is right pe end hone wale
                # saare valid subarrays ki count
                result += right - left + 1
            
            return result
        
        # Exactly k = at most k - at most (k-1)
        # Ye mathematical trick interviews mein gold hai
        return at_most_k(k) - at_most_k(k - 1)

#----Testing----
solver = Solution()
print(solver.subarraysWithKDistinct([1,2,1,2,3], 2))  # 7
print(solver.subarraysWithKDistinct([1,2,1,3,4], 3))  # 3