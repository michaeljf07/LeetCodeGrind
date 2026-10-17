from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0

        adj_map = defaultdict(list) # node -> (vertex, weight)
        for u, v, w in times:
            adj_map[u].append((v, w))
        
        heap = [(k, 0)]  # stores (node, path_weight)
        visited = set()
        while heap:
            node, path_weight = heapq.heappop(heap)
            if node in visited:
                continue
            
            visited.add(node)
            time = max(time, path_weight)

            for next_node, next_weight in adj_map[node]:
                if next_node not in visited:
                    heapq.heappush(heap, (next_node, time + next_weight))

        return time if len(visited) == n else -1
