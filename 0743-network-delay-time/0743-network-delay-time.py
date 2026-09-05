from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)  # source node -> (target node, time)
        for u, v, time in times:
            edges[u].append((v, time))

        min_heap = [(0, k)] # stores (total path, node)
        visited = set()
        time = 0

        while min_heap:
            weight, node = heapq.heappop(min_heap)
            # avoid cycles
            if node in visited:
                continue
            visited.add(node)
            time = max(time, weight)

            for nghbr_node, nghbr_weight in edges[node]:
                if nghbr_node not in visited:
                    heapq.heappush(min_heap, (weight + nghbr_weight, nghbr_node))
        
        return time if len(visited) == n else -1
