from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0:
            return 0
        
        # Character frequency window mein track karo
        char_count = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # Naya character window mein add karo
            char_count[s[right]] += 1
            
            # Agar distinct characters k se zyada ho gaye
            # Left se contract karo jab tak k distinct na ho jaaye
            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            
            # Current window size check karo
            max_len = max(max_len, right - left + 1)
        
        return max_len

#----Testing----
solver = Solution()
print(solver.lengthOfLongestSubstringKDistinct("eceba", 2))  # 3 ("ece")
print(solver.lengthOfLongestSubstringKDistinct("aa", 1))     # 2 ("aa")
print(solver.lengthOfLongestSubstringKDistinct("aabbc", 2))  # 4 ("aabb")