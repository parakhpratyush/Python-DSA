from collections import defaultdict
class Solution():
    def countComponents(self,n, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        components = 0
    
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
    
        return components

# Test
solver=Solution()
print(solver.countComponents(5, [[0,1],[1,2],[3,4]]))
print(solver.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))