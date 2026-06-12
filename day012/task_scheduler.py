from collections import Counter, deque
import heapq

def leastInterval(tasks, n):
    count = Counter(tasks)
    max_heap = [-cnt for cnt in count.values()]
    heapq.heapify(max_heap)
    
    time = 0
    waiting = deque()
    
    while max_heap or waiting:
        time += 1
        if max_heap:
            cnt = 1 + heapq.heappop(max_heap)
            if cnt:
                waiting.append((cnt, time + n))
        if waiting and waiting[0][1] == time:
            heapq.heappush(max_heap, waiting.popleft()[0])
    
    return time