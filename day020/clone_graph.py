class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution():
    def cloneGraph(self,node):
        if not node:
            return None
        cloned = {}
    
        def dfs(curr):
            if curr in cloned:
                return cloned[curr]
            clone = Node(curr.val)
            cloned[curr] = clone
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))
        
            return clone
    
        return dfs(node)
    
# 1. Setup the graph: 1 -- 2, 1 -- 4, 2 -- 3, 3 -- 4
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# 2. Test the solver
solver = Solution()
cloned_node1 = solver.cloneGraph(node1)

# Verification
print(f"Original Node Value: {node1.val}")
print(f"Cloned Node Value: {cloned_node1.val}")
print(f"Are they different objects? {node1 is not cloned_node1}")