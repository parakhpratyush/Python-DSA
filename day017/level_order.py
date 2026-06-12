from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution():
    def levelOrder(self,root):
        if not root:
            return []
    
        result = []  
        queue = deque([root]) 
    
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()        
                current_level.append(node.val) 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
    
        return result
    
root = TreeNode(3)
root.left=TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

solver=Solution()    
print(solver.levelOrder([]))
print(solver.levelOrder(TreeNode(1)))
print(solver.levelOrder(root))