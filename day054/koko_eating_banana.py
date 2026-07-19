import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = left + (right - left) // 2
            total_hours = 0
            
            for pile in piles:
                # Python 2 integer division truncates, so float conversion is safer for ceiling math
                total_hours += int(math.ceil(float(pile) / mid))
            
            if total_hours <= h:
                right = mid - 1
            else:
                left = mid + 1
                
        return left
