class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0
        
        # End time se sort karo — greedy classic
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        arrow_pos = points[0][1]
        
        for start, end in points[1:]:
            # Agar current balloon arrow se bahar hai
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end
        
        return arrows


#----Testing----
solver = Solution()
print(solver.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))   # 2
print(solver.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))      # 4
print(solver.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))      # 2