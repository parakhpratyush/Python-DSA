class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            # Ensure mid is even to check the pair starting at mid
            if mid % 2 == 1:
                mid -= 1
                
            # If the element at mid matches the next element,
            # the single element is further to the right.
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            # Otherwise, the single element is at mid or to the left.
            else:
                high = mid
                
        return nums[low]

#----Testing----
solver = Solution()

# Test Case 1
nums1 = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(solver.singleNonDuplicate(nums1))  # Expected Output: 2

# Test Case 2
nums2 = [3, 3, 7, 7, 10, 11, 11]
print(solver.singleNonDuplicate(nums2))  # Expected Output: 10
