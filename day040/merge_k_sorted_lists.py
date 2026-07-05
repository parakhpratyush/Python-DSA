import heapq

class Solution(object):
    def mergeKLists(self, lists):
        # Min heap use karo — hamesha smallest element top pe
        heap = []
        
        # Har list ka pehla element heap mein daalo
        for i, node in enumerate(lists):
            if node:
                # (value, index, node) — index isliye ki equal values pe comparison ho sake
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            
            # Is node ko result mein add karo
            current.next = node
            current = current.next
            
            # Is list ka next element heap mein daalo
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next

#----Testing----
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

solver = Solution()
lists = [make_list([1,4,5]), make_list([1,3,4]), make_list([2,6])]
print_list(solver.mergeKLists(lists))  # [1,1,2,3,4,4,5,6]