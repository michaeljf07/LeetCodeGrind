import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        res = [0] * len(queries)
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        sorted_queries = sorted([(query, i) for i, query in enumerate(queries)])
        visited = {(0, 0)}

        min_heap = [(grid[0][0], 0, 0)]  # (grid_val, row, col)
        points = 0

        for query_val, idx in sorted_queries:
            while min_heap and min_heap[0][0] < query_val:
                _, row, col = heapq.heappop(min_heap)
                points += 1

                for dx, dy in DIRECTIONS:
                    new_row, new_col = row + dx, col + dy
                    if (
                        0 <= new_row < ROWS and 0 <= new_col < COLS and
                        (new_row, new_col) not in visited
                    ):
                        visited.add((new_row, new_col))
                        heapq.heappush(min_heap, (grid[new_row][new_col], new_row, new_col))

            res[idx] = points

        return res