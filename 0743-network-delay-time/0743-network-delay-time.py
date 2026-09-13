from collections import defaultdict
import heapq


"""
Task: find the shortest path in a directed weighted graph
- Suited for Dijkstra's algorithm

Steps:
- Create an adjacency map
- 
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_map = defaultdict(list)
        for u, v, time in times:
            adj_map[u].append((v, time))

        min_heap = [(0, k)] # stores (path_so_far, node)
        visited = set()
        time = 0

        while min_heap:
            path_so_far, node = heapq.heappop(min_heap)
            # avoid cycles
            if node in visited:
                continue
            visited.add(node)

            time = max(time, path_so_far)
            
            for nghbr_node, nghbr_weight in adj_map[node]:
                if nghbr_node not in visited:
                    heapq.heappush(min_heap, (time + nghbr_weight, nghbr_node))

        return time if len(visited) == n else -1
