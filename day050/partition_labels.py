class Solution(object):
    def partitionLabels(self, s):
        # Har character ka last occurrence store karo
        last = {c: i for i, c in enumerate(s)}
        
        result = []
        start = 0
        end = 0
        
        for i, c in enumerate(s):
            # Current partition ka end extend karo
            # agar current char aage bhi hai toh
            end = max(end, last[c])
            
            # Partition complete — current index = end
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        
        return result

#----Testing----
solver = Solution()
print(solver.partitionLabels("ababcbacadefegdehijhklij"))
# [9, 7, 8]
print(solver.partitionLabels("eccbbbbdec"))
# [10]
