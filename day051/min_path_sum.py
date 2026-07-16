class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        
        # First row — sirf left se aa sakte hain
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        # First col — sirf upar se aa sakte hain
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        # Baaki cells — min(upar, left) + current
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]

#----Testing----
solver = Solution()
print(solver.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # 7
print(solver.minPathSum([[1,2,3],[4,5,6]]))           # 12
