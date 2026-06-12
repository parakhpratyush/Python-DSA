# Node class — ek single box jo tree mein rehti hai
class TreeNode:
    def __init__(self, val):
        # val → us node ki value store hoti hai
        self.val = val
        # left → left child ka reference (default None matlab koi child nahi)
        self.left = None
        # right → right child ka reference
        self.right = None

# Ab manually ek tree banao
root = TreeNode(1)      # root node banaya value 1 ke saath

root.left = TreeNode(2)   # root ke left mein 2
root.right = TreeNode(3)  # root ke right mein 3

root.left.left = TreeNode(4)   # 2 ke left mein 4
root.left.right = TreeNode(5)  # 2 ke right mein 5
root.right.right = TreeNode(6) # 3 ke right mein 6

# Ab ye tree ban gayi:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6


#1.INORDER-LEFT->ROOT->RIGHT
def inorder(node):
    # Base case — agar node None hai matlab hum tree ke bahar aa gaye
    # Kuch mat karo, wapas jao
    if node is None:
        return
    
    inorder(node.left)   # pehle poora left subtree visit karo
    print(node.val)       # phir current node print karo
    inorder(node.right)  # phir poora right subtree visit karo

inorder(root)
# Output: 4 2 5 1 3 6


#2.PREORDER-ROOT->LEFT->RIGHT
def preorder(node):
    # Base case same
    if node is None:
        return
    
    print(node.val)        # PEHLE current node print karo
    preorder(node.left)   # phir left subtree
    preorder(node.right)  # phir right subtree

preorder(root)
# Output: 1 2 4 5 3 6


#3.POSTORDER-LEFT->RIGHT->ROOT
def postorder(node):
    if node is None:
        return
    
    postorder(node.left)   # pehle left
    postorder(node.right)  # phir right
    print(node.val)         # AAKHIR MEIN current node

postorder(root)
# Output: 4 5 2 6 3 1


#4.LEVELORDER(BFS)_LEVEL-BY-LEVEL
from collections import deque

def level_order(root):
    if not root:
        return
    
    # Queue mein root daalo
    queue = deque([root])
    
    while queue:
        # Queue se ek node nikalo
        node = queue.popleft()
        print(node.val, end=" ")
        
        # Uske children queue mein daalo
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

level_order(root)
# Output: 1 2 3 4 5 6


#HEIGHT AUR DEPTH CALCULATION
def height(node):
    # Base case — None node ki height -1 ya 0 hoti hai
    # Hum 0 use karenge — leaf node ki height 0
    if node is None:
        return -1
    
    # Left subtree ki height nikalo recursively
    left_height = height(node.left)
    
    # Right subtree ki height nikalo recursively
    right_height = height(node.right)
    
    # Current node ki height = max(left, right) + 1
    # +1 isliye kyunki current node khud bhi count hoti hai
    return max(left_height, right_height) + 1

print("\nHeight:", height(root))  # 2