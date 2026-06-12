class Solution(object):
    def orangesRotting(self, grid):
        from collections import deque
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) 
                elif grid[r][c] == 1:
                    fresh += 1
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        time = 0

        while queue:
            r, c, t = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, t + 1))
                    time = t + 1
    
        return time if fresh == 0 else -1
object=Solution()    
print(object.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(object.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(object.orangesRotting([[0,2]]))