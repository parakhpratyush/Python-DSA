from collections import defaultdict
class Solution():
    def canFinish(self,numCourses, prerequisites):
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
    
   
        state = [0] * numCourses
    
        def has_cycle(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            state[node] = 1
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            state[node] = 2
            return False
        for course in range(numCourses):
            if state[course] == 0:
                if has_cycle(course):
                    return False
    
        return True

solver=Solution()
print(solver.canFinish(2,[[1,0]]))   
print(solver.canFinish(2,[[1,0],[0,1]]))

