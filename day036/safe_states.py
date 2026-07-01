class Solution():
    def eventualSafeNodes(self,graph):
        n = len(graph)
        state = [0] * n
    
        def dfs(node):
            if state[node] == 1:  
                return False
            if state[node] == 2:  
                return True
        
            state[node] = 1 
        
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False 
        
            state[node] = 2  
            return True
    
        return [i for i in range(n) if dfs(i)]
    
#----Testing----
solver=Solution()

print(solver.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
print(solver.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))