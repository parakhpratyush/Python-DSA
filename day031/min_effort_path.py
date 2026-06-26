import heapq
class Solution():
    def minimumEffortPath(self,heights):
        rows, cols = len(heights), len(heights[0])
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0
    
        pq = [(0, 0, 0)]  # (effort, row, col)
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
        while pq:
            curr_effort, r, c = heapq.heappop(pq)
        
            if r == rows-1 and c == cols-1:
                return curr_effort
        
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(curr_effort, abs(heights[nr][nc] - heights[r][c]))
                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))
    
        return 
    
#----Testing----
solver=Solution()

print(solver.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
print(solver.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
print(solver.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))