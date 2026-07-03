class UnionFind:
    def __init__(self, n):
        # Pehle har node apna khud ka parent hai
        self.parent = list(range(n))
        # Rank = tree ki depth, merge optimize karne ke liye
        self.rank = [0] * n
    
    def find(self, x):
        # Path compression — seedha root pe point karo
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already same group mein hain
        # Chote rank wale ko bade rank ke neeche daalo
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True