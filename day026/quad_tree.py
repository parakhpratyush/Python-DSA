class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
class Solution():
    def construct(self,grid):
        n = len(grid)
    
        def solve(row, col, size):
            first_val = grid[row][col]
            is_uniform = True
        
            for i in range(row, row + size):
                for j in range(col, col + size):
                    if grid[i][j] != first_val:
                        is_uniform = False
                        break
                if not is_uniform:
                    break
        
            if is_uniform:
                return Node(first_val == 1, True, None, None, None, None)
            half = size // 2
            tl = solve(row, col, half)
            tr = solve(row, col + half, half)
            bl = solve(row + half, col, half)
            br = solve(row + half, col + half, half)
        
            return Node(True, False, tl, tr, bl, br)
    
        return solve(0, 0, n)

def get_leetcode_list(root):
    if not root: return []
    result, queue = [], [root]
    while queue:
        curr = queue.pop(0)
        if curr:
            result.append([1 if curr.isLeaf else 0, 1 if curr.val else 0])
            if not curr.isLeaf:
                queue.extend([curr.topLeft, curr.topRight, curr.bottomLeft, curr.bottomRight])
    return result

# --- TESTING ---
grid1 = [[0, 1], [1, 0]]
grid2 = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]

solver = Solution()

root1 = solver.construct(grid1)
root2 = solver.construct(grid2)
print(get_leetcode_list(root1))
print(get_leetcode_list(root2))
