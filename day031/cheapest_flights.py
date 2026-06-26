class Solution():
    def findCheapestPrice(self,n, flights, src, dst, k):
        distances = [float('inf')] * n
        distances[src] = 0
        for _ in range(k + 1):
            temp = distances[:]
            for u, v, w in flights:
                if distances[u] != float('inf') and distances[u] + w < temp[v]:
                    temp[v] = distances[u] + w
            distances = temp
    
        return distances[dst] if distances[dst] != float('inf') else -1

#----Testing----
solver=Solution()

print(solver.findCheapestPrice(n =
4,
flights =
[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
src =
0,
dst =
3,
k =
1))
print(solver.findCheapestPrice(n =
3,
flights =
[[0,1,100],[1,2,100],[0,2,500]],
src =
0,
dst =
2,
k =
1))
print(solver.findCheapestPrice(n =
3,
flights =
[[0,1,100],[1,2,100],[0,2,500]],
src =
0,
dst =
2,
k =
0))