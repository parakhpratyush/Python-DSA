class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                return
            curr = curr.next
    
    def print_list(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" → ".join(elements) + " → None")
    
    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

# Test
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
ll.print_list() 
ll.delete(2)
ll.print_list() 
print("Length:", ll.length()) 