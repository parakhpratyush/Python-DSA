class Solution(object):
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Negative contributions ignore karo — 0 lo unki jagah
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # Is node se guzarne wala path sum check karo
            current_path = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path)
            
            # Parent ko sirf ek side return karo
            # Kyun? Parent ke saath path mein dono sides simultaneously nahi aa sakti
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return self.max_sum

#----Testing----
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

solver = Solution()

# Tree: [-10, 9, 20, null, null, 15, 7]
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(solver.maxPathSum(root))   # 42 (15+20+7)

# Tree: [1, 2, 3]
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
print(solver.maxPathSum(root2))  # 6