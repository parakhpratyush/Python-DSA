class Solution():
    def largestRectangleArea(self,heights):
        stack = []
        max_area = 0
        heights = heights + [0]
    
        for i, h in enumerate(heights):
            start = i
        
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
        
            stack.append((start, h))
    
        return max_area

#----Testing----
solver=Solution()

print(solver.largestRectangleArea([2,1,5,6,2,3]))
print(solver.largestRectangleArea([2,4])) 