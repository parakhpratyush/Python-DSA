class Solution():
    def merge_intervals(self,intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
    
        merged = [intervals[0]]
    
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
    
        return merged

#----Testing----

solver=Solution()

print(solver.merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
print(solver.merge_intervals([[1,4],[4,5]]))
print(solver.merge_intervals([[4,7],[1,4]]))

