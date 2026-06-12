class Solution(object):
    def minimumCost(cost):
        cost.sort(reverse=True)
        total_cost = 0
        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
            
        return total_cost
    
print(Solution.minimumCost([1,2,3]))
print(Solution.minimumCost([6,5,7,9,2,2]))
print(Solution.minimumCost([5,5]))