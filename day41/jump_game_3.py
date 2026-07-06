class Solution(object):
    def canReach(self, arr, start):
        n = len(arr)
        visited = set()
        stack = [start]
        
        while stack:
            i = stack.pop()
            if i < 0 or i >= n or i in visited:
                continue
            if arr[i] == 0:
                return True
            visited.add(i)
            stack.append(i + arr[i])
            stack.append(i - arr[i])
        
        return False

#----Testing----
solver = Solution()
print(solver.canReach([4,2,3,0,3,1,2], 5))   # True
print(solver.canReach([4,2,3,0,3,1,2], 0))   # True
print(solver.canReach([3,0,2,1,2], 2))        # False
