from collections import defaultdict, deque

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        
        # Stop → routes mapping
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        
        visited_stops = {source}
        visited_routes = set()
        queue = deque([source])
        buses = 0
        
        while queue:
            buses += 1
            for _ in range(len(queue)):
                stop = queue.popleft()
                for route_id in stop_to_routes[stop]:
                    if route_id in visited_routes:
                        continue
                    visited_routes.add(route_id)
                    for next_stop in routes[route_id]:
                        if next_stop == target:
                            return buses
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append(next_stop)
        
        return -1

#----Testing----
solver = Solution()
print(solver.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))   # 2
print(solver.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))  # -1