class Solution(object):
    def topKFrequent(nums, k):
        from collections import Counter
        from collections import defaultdict
        gra = defaultdict(int)
        for char in nums:
            gra[char]+=1
        g=Counter(gra)
        return list(zip(*g.most_common(k)))[0]

print(Solution.topKFrequent([1,1,1,2,2,3],2))
print(Solution.topKFrequent([1],1))
print(Solution.topKFrequent([1,2,1,2,1,2,3,1,3,2],2))