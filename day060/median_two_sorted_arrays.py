class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to optimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2
        
        while low <= high:
            # Partition index for nums1
            i = (low + high) // 2
            # Partition index for nums2
            j = total_left - i
            
            # Boundary values around partition
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            # Check if partition is correct
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # If total elements are odd
                if (m + n) % 2 == 1:
                    return float(max(nums1_left_max, nums2_left_max))
                # If total elements are even
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            
            # Adjust binary search window
            elif nums1_left_max > nums2_right_min:
                high = i - 1
            else:
                low = i + 1
                
        return 0.0

#----Testing----
solver=Solution()

print(solver.findMedianSortedArrays([1, 3], [2]))
print(solver.findMedianSortedArrays([1, 2], [3, 4]))
