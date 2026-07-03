class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        # Unique roots = number of provinces
        return len(set(find(i) for i in range(n)))

#----Testing----
solver = Solution()
print(solver.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  # 2
print(solver.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))  # 3