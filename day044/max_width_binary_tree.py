from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        
        max_width = 0
        # (node, index) — index se width calculate karenge
        queue = deque([(root, 0)])
        
        while queue:
            level_len = len(queue)
            _, first_idx = queue[0]
            
            for _ in range(level_len):
                node, idx = queue.popleft()
                # Normalize index to prevent overflow
                idx -= first_idx
                
                if node.left:
                    queue.append((node.left, 2 * idx))
                if node.right:
                    queue.append((node.right, 2 * idx + 1))
            
            last_idx = idx
            max_width = max(max_width, last_idx - 0 + 1)
        
        return max_width


#----Testing----
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

solver = Solution()
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
print(solver.widthOfBinaryTree(root))   # 4