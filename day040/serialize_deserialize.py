from collections import deque

class Codec(object):

    def serialize(self, root):
        # BFS se tree ko string mein convert karo
        if not root:
            return "null"
        
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        return ",".join(result)

    def deserialize(self, data):
        if data == "null":
            return None
        
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1
        
        while queue and i < len(nodes):
            node = queue.popleft()
            
            # Left child
            if nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1
            
            # Right child
            if i < len(nodes) and nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        
        return root

#----Testing----
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

solver = Codec()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

serialized = solver.serialize(root)
print("Serialized:", serialized)

deserialized = solver.deserialize(serialized)
print("Root val:", deserialized.val)           # 1
print("Left val:", deserialized.left.val)      # 2
print("Right val:", deserialized.right.val)    # 3