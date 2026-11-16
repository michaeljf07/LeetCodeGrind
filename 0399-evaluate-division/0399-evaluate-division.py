from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        adj_map = defaultdict(list)  # variable -> (connected var, val of division)
        for i, eqn in enumerate(equations):
            a, b = eqn
            adj_map[a].append((b, values[i]))
            adj_map[b].append((a, 1 / values[i]))  # inverse of division value given

        def dfs(src: str, target: str, visited: set[int]):
            if src not in adj_map or target not in adj_map:
                return -1
            if src == target:
                return 1

            visited.add(src)

            # we are looking to calculate src/target
            # this is equivalenet to src/nghbr * nghrb/target (with any number  neighbors)
            for nghbr, weight in adj_map[src]:
                if nghbr in visited:
                    continue
                result = dfs(nghbr, target, visited)
                if result != -1:
                    return weight * result

            return -1

        return [dfs(src, target, set()) for src, target in queries]
