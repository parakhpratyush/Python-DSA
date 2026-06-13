class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def isValidBST(self,root):
        def validate(node, min_val, max_val):
            if node is None:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            left_valid = validate(node.left, min_val, node.val)
            right_valid = validate(node.right, node.val, max_val)
            return left_valid and right_valid
        return validate(root, float('-inf'), float('+inf'))
    
    def printTree(self, root, res=[]):
        queue = [root] if root else []
        for node in queue:
            if node: res.append(node.val); queue.extend([node.left, node.right])
        return [x for x in res if x is not None]
    
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

solver=Solution()

# Test Case 1:
print("first root structure:", solver.printTree(root,[]))
res1 = solver.isValidBST(root)
print("Is Test 1 a Valid BST?:", res1)

print("-" * 100)

#----------------------------------------

# Test Case 2:
print("first root structure:", solver.printTree(root1,[]))
res2 = solver.isValidBST(root1)
print("Is Test 1 a Valid BST?:", res2)