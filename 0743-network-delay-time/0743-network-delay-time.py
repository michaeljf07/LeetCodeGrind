from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_map = defaultdict(list)  # node -> (neighbor, weight)
        for u, v, w in times:
            adj_map[u].append((v, w))
        
        heap = [(0, k)]  # stores (path_weight, node)
        visited = set()
        max_time = 0

        while heap:
            path_weight, node = heapq.heappop(heap)
            
            if node in visited:
                continue
            
            visited.add(node)
            max_time = path_weight

            for next_node, weight in adj_map[node]:
                if next_node not in visited:
                    heapq.heappush(heap, (path_weight + weight, next_node))

        return max_time if len(visited) == n else -1
