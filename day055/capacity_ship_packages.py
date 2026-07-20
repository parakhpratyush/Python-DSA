class Solution:
    def shipWithinDays(self, weights,days):
        def canShip(capacity):
            current_days = 1
            current_weight = 0
            
            for w in weights:
                if current_weight + w > capacity:
                    current_days += 1
                    current_weight = 0
                current_weight += w
                
            return current_days <= days

        low = max(weights)
        high = sum(weights)
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            if canShip(mid):
                result = mid       # Try to find a smaller valid capacity
                high = mid - 1
            else:
                low = mid + 1      # Mid is too small, increase capacity
                
        return result
      
#----Testing-----
solver=Solution()

print(solver.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))
print(solver.shipWithinDays(weights = [3,2,2,4,1,4], days = 3))
print(solver.shipWithinDays(weights = [1,2,3,1,1], days = 4))
