from collections import defaultdict, deque
class Solution():
    def minimumSemesters(self,n, relations):
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
    
        for prev, next_course in relations:
            graph[prev].append(next_course)
            indegree[next_course] += 1
    
        queue = deque([i for i in range(1, n+1) if indegree[i] == 0])
        semesters = 0
        taken = 0
    
        while queue:
            semesters += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                taken += 1
                for next_course in graph[course]:
                    indegree[next_course] -= 1
                    if indegree[next_course] == 0:
                        queue.append(next_course)
    
        return semesters if taken == n else -1

#----Testing----
solver=Solution()

if __name__ == "__main__":
    print("\n" + "="*50)
    print("⚡ TESTING LEETCODE #1136: PARALLEL COURSES")
    print("="*50)
    
    # Test Case 1: Valid Parallel Multitasking Sequence
    n1, rel1 = 3, [[1,3],[2,3]]
    print(f"Test 1 Setup: Nodes={n1}, Relations={rel1}")
    print(f"Output Semesters: {solver.minimumSemesters(n1, rel1)} | Expected: 2\n")
    
    # Test Case 2: Deadlock Dependency Cycle
    n2, rel2 = 3, [[1,2],[2,3],[3,1]]
    print(f"Test 2 Setup: Nodes={n2}, Relations={rel2}")
    print(f"Output Semesters: {solver.minimumSemesters(n2, rel2)} | Expected: -1 (Unresolvable Cycle)")
    print("="*50)