class LRUCache(object):
    
    class Node:
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        # Dummy head aur tail — edge cases handle karne ke liye
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        # Node ko DLL se remove karo
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insert_front(self, node):
        # Node ko head ke baad insert karo (most recently used)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key):
        if key not in self.cache:
            return -1
        # Node ko front pe le aao (recently used)
        node = self.cache[key]
        self._remove(node)
        self._insert_front(node)
        return node.val
    
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = self.Node(key, value)
        self._insert_front(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            # Tail se pehle wala = least recently used
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

#----Testing----
solver = LRUCache(2)
solver.put(1, 1)
solver.put(2, 2)
print(solver.get(1))   
solver.put(3, 3)       
print(solver.get(2))  
print(solver.get(3))   