from collections import defaultdict, deque

def topological_sort_bfs(n, edges):
    # Kahn's Algorithm — BFS based
    graph = defaultdict(list)
    indegree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    
    # Sabse pehle wo nodes jinka indegree 0 hai
    queue = deque([i for i in range(n) if indegree[i] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Agar saare nodes nahi aaye — cycle hai
    return order if len(order) == n else []


def topological_sort_dfs(n, edges):
    # DFS based — finish time reverse order
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    visited = set()
    stack = []
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)  # Post-order mein add karo
    
    for i in range(n):
        if i not in visited:
            dfs(i)
    
    return stack[::-1]  # Reverse = topological order


# Test
edges = [(0,1),(0,2),(1,3),(2,3)]
print(topological_sort_bfs(4, edges))  # [0,1,2,3] or [0,2,1,3]
print(topological_sort_dfs(4, edges))