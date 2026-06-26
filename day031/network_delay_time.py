import heapq
from collections import defaultdict
class Solution():
    def networkDelayTime(times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
    
        distances = {i: float('inf') for i in range(1, n+1)}
        distances[k] = 0
        pq = [(0, k)]
        visited = set()
    
        while pq:
            d, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
        
            for neighbor, weight in graph[node]:
                new_dist = d + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
    
        max_dist = max(distances.values())
        return max_dist if max_dist != float('inf') else -1

#----Testing----
solver=Solution()

print(solver.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(solver.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
print(solver.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))