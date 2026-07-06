import heapq

class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while heap:
            t, r, c = heapq.heappop(heap)
            
            if r == n-1 and c == n-1:
                return t
            
            if (r, c) in visited:
                continue
            visited.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited:
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
        
        return -1

#----Testing----
solver = Solution()
print(solver.swimInWater([[0,2],[1,3]]))                        # 3
print(solver.swimInWater([[0,1,2,3,4],[24,23,22,21,5],
                           [12,13,14,15,16],[11,17,18,19,20],
                           [10,9,8,7,6]]))                      # 16
