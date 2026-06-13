class TreeNode:
    def __init__(self, val):
        # val → is node mein stored integer value
        self.val = val
        # left → left child ka reference, initially koi child nahi
        self.left = None
        # right → right child ka reference, initially koi child nahi
        self.right = None

class BST:
    def __init__(self):
        # root → poore tree ka starting point
        # Jab tree empty hota hai root = None
        self.root = None
    
    def insert(self, val):
        # Agar tree bilkul khali hai, naya node hi root ban jaata hai
        if not self.root:
            self.root = TreeNode(val)
            return
        # Warna helper function call karo
        self._insert_helper(self.root, val)
    
    def _insert_helper(self, node, val):
        # val chota hai current node se → left side jaao
        if val < node.val:
            # Agar left child exist nahi karta → wahan daal do
            if node.left is None:
                node.left = TreeNode(val)
            else:
                # Left child exist karta hai → recursively us pe jaao
                self._insert_helper(node.left, val)
        
        # val bada hai current node se → right side jaao
        else:
            # Agar right child exist nahi karta → wahan daal do
            if node.right is None:
                node.right = TreeNode(val)
            else:
                # Right child exist karta hai → recursively us pe jaao
                self._insert_helper(node.right, val)
    
    def search(self, val):
        # Root se search shuru karo
        return self._search_helper(self.root, val)
    
    def _search_helper(self, node, val):
        # Base case 1: Node hi nahi mila → value tree mein nahi hai
        if node is None:
            return False
        
        # Base case 2: Current node ki value match karti hai → MILA!
        if node.val == val:
            return True
        
        # val chota hai → left mein dhoondho
        if val < node.val:
            return self._search_helper(node.left, val)
        
        # val bada hai → right mein dhoondho
        else:
            return self._search_helper(node.right, val)
    
    def inorder(self):
        # Inorder traversal BST mein sorted order deta hai — YE MAGIC HAI
        result = []
        self._inorder_helper(self.root, result)
        return result
    
    def _inorder_helper(self, node, result):
        if node is None:
            return
        # Pehle left (chote values)
        self._inorder_helper(node.left, result)
        # Phir current node
        result.append(node.val)
        # Phir right (bade values)
        self._inorder_helper(node.right, result)


# TEST KARO
tree = BST()
# Ye values insert karo ek ek karke
for val in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    tree.insert(val)

# Search test
print("6 hai tree mein?", tree.search(6))   # True
print("5 hai tree mein?", tree.search(5))   # False

# Inorder → sorted output aana chahiye
print("Inorder:", tree.inorder())  # [1, 3, 4, 6, 7, 8, 10, 13, 14]