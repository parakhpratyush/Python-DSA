from collections import defaultdict, deque
class Solution():
    def alienOrder(self,words):
        adj = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}
    
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
        
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        queue = deque([c for c in indegree if indegree[c] == 0])
        result = []
    
        while queue:
            c = queue.popleft()
            result.append(c)
            for neighbor in adj[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
    
        return "".join(result) if len(result) == len(indegree) else ""
    
# ----Testing----
solver=Solution()

if __name__ == "__main__":
    print("="*50)
    print("⚡ TESTING LEETCODE #269: ALIEN DICTIONARY")
    print("="*50)
    
    # Test Case 1: Standard Valid Sequencing Network
    t1 = ["wrt","wrf","er","ett","rft"]
    print(f"Test 1 Inputs: {t1}")
    print(f"Output Matrix: '{solver.alienOrder(t1)}' | Expected: 'wertf'\n")
    
    # Test Case 2: Unresolvable Cyclic Loop
    t2 = ["z","x","z"]
    print(f"Test 2 Inputs: {t2}")
    print(f"Output Matrix: '{solver.alienOrder(t2)}' | Expected: '' (Cycle Found)\n")
    
    # Test Case 3: Invalid Suffix/Prefix Length Breakdown
    t3 = ["abc","ab"]
    print(f"Test 3 Inputs: {t3}")
    print(f"Output Matrix: '{solver.alienOrder(t3)}' | Expected: '' (Prefix Mismatch)")
    print("="*50)