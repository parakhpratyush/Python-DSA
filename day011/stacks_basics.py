# Stack implementation
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Test it
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Peek:", s.peek())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Size:", s.size())
print("Empty?", s.is_empty())