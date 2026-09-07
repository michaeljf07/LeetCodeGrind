class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        visit = [False] * n  # visit[i] = whether point i is already in the MST
        dist = [float("inf")] * n  # dist[i] = min cost to connect point i to the current MST
        
        curr_node = 0
        connected_edges = 0
        res = 0

        while connected_edges < n - 1:
            visit[curr_node] = True
            
            # update distances from curr_node to all unvisited nodes
            for i in range(n):
                if not visit[i]:
                    d = self.calc_distance(points[curr_node], points[i])
                    dist[i] = min(dist[i], d)

            # opick the unvisited node with the smallest distance to the MST
            next_node = -1
            for i in range(n):
                if not visit[i]:
                    if next_node == -1 or dist[i] < dist[next_node]:
                        next_node = i
            
            # add this edge to the MST
            res += dist[next_node]
            curr_node = next_node
            connected_edges += 1
            
        return res

    @staticmethod
    def calc_distance(p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])