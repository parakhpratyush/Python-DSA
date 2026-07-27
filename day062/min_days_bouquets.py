class Solution(object):
    def minDays(self, bloomDay, m, k):
        # Base check: total flowers needed vs available
        if m * k > len(bloomDay):
            return -1

        # Move helper outside or define before loop
        def canMake(days):
            bouquets = 0
            flowers = 0
            
            for d in bloomDay:
                if d <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                        # Early exit optimization: stop iterating once goal is reached
                        if bouquets >= m:
                            return True
                else:
                    flowers = 0
            
            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if canMake(mid):
                ans = mid
                right = mid - 1  # Try to find a smaller day
            else:
                left = mid + 1   # Need more days

        return ans

solver = Solution()

# Test Case 1: Standard case where flowers bloom at different times
bloomDay1 = [1, 10, 3, 10, 2]
m1, k1 = 3, 1
# Explanation: Day 3 lets flowers at index 0, 2, 4 bloom -> 3 bouquets of size 1.
print("Test 1:", solver.minDays(bloomDay1, m1, k1))  # Expected: 3

# Test Case 2: Impossible because total required flowers (3*2=6) > len(bloomDay) (5)
bloomDay2 = [1, 10, 3, 10, 2]
m2, k2 = 3, 2
print("Test 2:", solver.minDays(bloomDay2, m2, k2))  # Expected: -1

# Test Case 3: Requires adjacent flowers blooming by the target day
bloomDay3 = [7, 7, 7, 7, 12, 7, 7]
m3, k3 = 2, 3
# Explanation: Day 12 allows all flowers to bloom, giving two adjacent groups of 3.
print("Test 3:", solver.minDays(bloomDay3, m3, k3))  # Expected: 12

# Test Case 4: All flowers bloom on day 1
bloomDay4 = [1, 1, 1, 1]
m4, k4 = 2, 2
print("Test 4:", solver.minDays(bloomDay4, m4, k4))  # Expected: 1

# Test Case 5: Single bouquet requiring all elements
bloomDay5 = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
m5, k5 = 1, 10
print("Test 5:", solver.minDays(bloomDay5, m5, k5))  # Expected: 10
