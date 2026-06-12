class Solution(object):
    def maxProfit(prices):
        minprices=float("inf")
        maxProfit=0
        for i in prices:
            if i<minprices:
                minprices=i
            currentproffit=i-minprices
            if currentproffit>maxProfit:
                maxProfit=currentproffit
        return(maxProfit)
        
print(Solution.maxProfit([9,3,7,4,5,6]))

            
             