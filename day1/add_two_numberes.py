class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      
        self.next = next

class Solution(object):
    def add_two_numbers(l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
    
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
        
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
        
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
    
        return dummy.next

#for testing the correctness of code
def make_list(nums):
    dummy = ListNode(0)
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

l1 = make_list([2, 4, 3])
l2 = make_list([5, 6, 4])
result =Solution.add_two_numbers(l1,l2)

while result:
    print(result.val, end=" -> ")
    result = result.next




