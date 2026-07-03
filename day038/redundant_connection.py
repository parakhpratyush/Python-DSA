class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False  # Ye edge redundant hai — cycle ban rahi hai
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        return []

#----Testing----
solver = Solution()
print(solver.findRedundantConnection([[1,2],[1,3],[2,3]]))    # [2,3]
print(solver.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # [1,4]