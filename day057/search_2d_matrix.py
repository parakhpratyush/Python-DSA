class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # Start at the top-right corner
        row = 0
        col = len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            current = matrix[row][col]
            
            if current == target:
                return True
            elif current > target:
                # Target is smaller; eliminate this entire column
                col -= 1
            else:
                # Target is larger; eliminate this entire row
                row += 1
                
        return False

#----Testing----
solver=Solution()

print(solver.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(solver.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))