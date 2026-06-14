from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # defaultdict(list) — agar key exist nahi karti
        # toh automatically empty list create ho jaati hai
        # Normal dict mein KeyError aata, yahan nahi aayega
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        # Undirected graph — dono taraf connection add karo
        # u → v aur v → u dono
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, start):
        # visited = set because lookup O(1) hota hai set mein
        # list mein O(n) hota — slow hoga large graphs mein
        visited = set()
        
        # Queue mein starting node daalo
        # deque isliye kyunki popleft() O(1) hai
        # list ka pop(0) O(n) hai — NEVER use list as queue
        queue = deque([start])
        result = []
        
        while queue:
            # Queue se FRONT node nikalo — FIFO
            node = queue.popleft()
            
            # Agar pehle visit nahi kiya
            if node not in visited:
                visited.add(node)    # mark karo
                result.append(node)  # result mein daalo
                
                # Is node ke SAARE neighbors queue mein daalo
                # Visited check isliye taaki infinite loop na ho
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result
    
    def dfs_recursive(self, start, visited=None):
        # Pehli call pe visited None hoga
        # Default argument mutable nahi hona chahiye
        # isliye None check karo aur wahan set banao
        if visited is None:
            visited = set()
        
        # Current node mark karo
        visited.add(start)
        result = [start]
        
        # Har neighbor pe DFS recursively call karo
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                # extend matlab list ke saare elements add karo
                # append sirf ek element add karta hai
                result.extend(self.dfs_recursive(neighbor, visited))
        
        return result
    
    def dfs_iterative(self, start):
        # Recursion stack overflow de sakta hai deep graphs mein
        # Iterative version explicit stack use karta hai
        visited = set()
        
        # Stack mein starting node daalo
        # List as stack — append = push, pop() = pop from top
        stack = [start]
        result = []
        
        while stack:
            # Stack se TOP element nikalo — LIFO
            node = stack.pop()
            
            if node not in visited:
                visited.add(node)
                result.append(node)
                
                # Neighbors stack mein daalo
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result


# Test karo
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

print("BFS from 1:", g.bfs(1))
print("DFS recursive from 1:", g.dfs_recursive(1))
print("DFS iterative from 1:", g.dfs_iterative(1))