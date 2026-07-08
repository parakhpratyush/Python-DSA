class Solution(object):
    def countSmaller(self, nums):
        # Coordinate compression + BIT (Binary Indexed Tree)
        sorted_unique = sorted(set(nums))
        rank = {v: i+1 for i, v in enumerate(sorted_unique)}
        n = len(sorted_unique)
        
        bit = [0] * (n + 1)
        
        def update(i):
            while i <= n:
                bit[i] += 1
                i += i & (-i)
        
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
        
        result = []
        for num in reversed(nums):
            r = rank[num]
            result.append(query(r - 1))
            update(r)
        
        return result[::-1]

#----Testing----
solver = Solution()
print(solver.countSmaller([5,2,6,1]))    # [2,1,1,0]
print(solver.countSmaller([-1,-1]))      # [0,0]