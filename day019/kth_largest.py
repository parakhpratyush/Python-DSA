import heapq
class Solution():
    def findKthLargest(self,nums, k):
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]

# Test
solver=Solution()
print(solver.findKthLargest([3,2,1,5,6,4], 2))
print(solver.findKthLargest([3,2,3,1,2,4,5,5,6], 4))