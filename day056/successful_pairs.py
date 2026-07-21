import math
import bisect

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        # Sort potions to enable binary search
        potions.sort()
        m = len(potions)
        pairs = []
        
        for spell in spells:
            # Find the minimum potion strength needed using ceiling division
            # (success + spell - 1) // spell is equivalent to math.ceil(success / spell)
            min_potion = (success + spell - 1) // spell
            
            # Find the first index where the potion strength >= min_potion
            idx = bisect.bisect_left(potions, min_potion)
            
            # All elements from 'idx' to the end are valid pairs
            pairs.append(m - idx)
            
        return pairs


#----Testing----
solver = Solution()

# Test Case 1: Standard case with sorted/unsorted inputs
print(solver.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7)) # Output: [4, 0, 3]

# Test Case 2: Large success threshold
print(solver.successfulPairs([3, 1, 2], [8, 5, 8], 16))