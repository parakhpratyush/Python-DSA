class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def kthSmallest(self,root, k):
        stack = []
        current = root
        count = 0
    
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
        
            current = stack.pop()
            count += 1
        
            if count == k:
                return current.val
        
            current = current.right

# --- TESTING ENGINES ---

# Test Case 1: root = [3,1,4,null,2], k = 1
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.left.right = TreeNode(2)

solver = Solution()
print("Output :", solver.kthSmallest(root1, k=1))

print("---------------------------------------------------------------------------------------------------------------------------------------")

# Test Case 2: root = [5,3,6,2,4,null,null,1], k = 3
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.left.left.left = TreeNode(1)

print("Output :", solver.kthSmallest(root2, k=3))