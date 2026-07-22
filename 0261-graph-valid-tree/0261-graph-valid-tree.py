class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node: int, prev: int) -> bool:
            # Cycle detected
            if node in visited:
                return False

            visited.add(node)
            for nghbr in adj[node]:
                # Prevent repeating checked nodes
                if nghbr == prev:
                    continue
                if not dfs(nghbr, node):
                    return False

            return True

        is_graph_acyclic = dfs(0, -1)
        is_graph_connected = len(visited) == n
        return is_graph_acyclic and is_graph_connected
