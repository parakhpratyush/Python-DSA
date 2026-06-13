class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def searchBST(self,root, val):
        if root is None or root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)        
solver=Solution()  

# Test Case 1:
res1 = solver.searchBST(root, 2)
if res1:
    print("Test 1 Result:", res1.val)
else:
    print("Test 1 Result: None")

#----------------------------------------

# Test Case 2:
res2 = solver.searchBST(root, 5)
if res2:
    print("Test 2 Result:", res2.val)
else:
    print("Test 2 Result: Node not found (Safely caught None)")