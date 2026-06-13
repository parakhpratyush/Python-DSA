class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def insertIntoBST(self,root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
    
    def printTree(self, root, res=[]):
        queue = [root] if root else []
        for node in queue:
            if node: res.append(node.val); queue.extend([node.left, node.right])
        return [x for x in res if x is not None]
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root1 = TreeNode(40)
root1.left = TreeNode(20)
root1.right = TreeNode(60)
root1.left.left = TreeNode(10)
root1.left.right = TreeNode(30)
root1.right.left = TreeNode(50)
root1.right.right = TreeNode(70)

root2 = TreeNode(4)
root2.left = TreeNode(2)
root2.right = TreeNode(7)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)

solver=Solution()

# Test Case 1:
print("first root bofore was:",solver.printTree(root,[]))
res1 = solver.insertIntoBST(root, 5)
if res1:
    print("after Test 1 is       ", solver.printTree(res1,[]))
else:
    print("Test 1 Result: None")

print("-" * 50)

#----------------------------------------

# Test Case 2:
print("second root bofore was:",solver.printTree(root1,[]))
res2 = solver.insertIntoBST(root1, 25)
if res2:
    print("after Test 2 is        ", solver.printTree(res2,[]))
else:
    print("Test 2 Result: None")

print("-" * 50)

#----------------------------------------

# Test Case 3:
print("third root bofore was:",solver.printTree(root2,[]))
res3 = solver.insertIntoBST(root2, 5)
if res3:
    print("after Test 3 is       ", solver.printTree(res3,[]))
else:
    print("Test 3 Result: None")
