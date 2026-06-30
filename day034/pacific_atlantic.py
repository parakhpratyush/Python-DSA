class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights:
            return []
    
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
    
        def dfs(r, c, visited, prev_height):
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                (r, c) in visited or heights[r][c] < prev_height):
                return
        
            visited.add((r, c))
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                dfs(r+dr, c+dc, visited, heights[r][c])
    
        for c in range(cols):
            dfs(0, c, pacific, 0)
            dfs(rows-1, c, atlantic, 0)
    
        for r in range(rows):
            dfs(r, 0, pacific, 0)
            dfs(r, cols-1, atlantic, 0)
    
        return list(pacific & atlantic)

#----Testing----    
solver=Solution()

print(solver.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(solver.pacificAtlantic([[1]]))