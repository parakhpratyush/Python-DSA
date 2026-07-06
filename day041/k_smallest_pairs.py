import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        
        heap = []
        result = []
        
        # Pehle nums1 ke saare elements nums2[0] ke saath push karo
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        while heap and len(result) < k:
            total, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            # Same nums1[i] ke saath nums2 ka next element push karo
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
        
        return result

#----Testing----
solver = Solution()
print(solver.kSmallestPairs([1,7,11], [2,4,6], 3))   # [[1,2],[1,4],[1,6]]
print(solver.kSmallestPairs([1,1,2], [1,2,3], 2))    # [[1,1],[1,1]]
