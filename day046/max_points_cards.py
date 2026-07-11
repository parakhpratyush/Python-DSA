class Solution(object):
    def maxScore(self, cardPoints, k):
        # Total window size = n - k (beech wala part)
        # Minimum beech wala = Maximum ends wala
        n = len(cardPoints)
        window_size = n - k
        
        # Pehli window ka sum
        current_sum = sum(cardPoints[:window_size])
        min_sum = current_sum
        
        for i in range(window_size, n):
            current_sum += cardPoints[i] - cardPoints[i - window_size]
            min_sum = min(min_sum, current_sum)
        
        return sum(cardPoints) - min_sum

#----Testing----
solver = Solution()
print(solver.maxScore([1,2,3,4,5,6,1], 3))   # 12
print(solver.maxScore([2,2,2], 2))             # 4
print(solver.maxScore([9,7,7,9,7,7,9], 7))    # 55