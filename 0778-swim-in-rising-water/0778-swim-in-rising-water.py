class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        # the path through the grid can be modelled as a weighted graph where the costs (weights)
        # between nodes is the maximum height (time to wait) between the cells
        min_heap = [(grid[0][0], 0, 0)]  # min_heap stores (time_so_far, row, col)
        visited = {(0, 0)}

        while min_heap:
            time_so_far, row, col = heapq.heappop(min_heap)

            # we have reached our destination
            if (row, col) == (ROWS - 1, COLS - 1):
                return time_so_far

            for dx, dy in DIRECTIONS:
                new_row, new_col = row + dx, col + dy
                if (
                    new_row < 0
                    or new_row >= ROWS
                    or new_col < 0
                    or new_col >= COLS
                    or (new_row, new_col) in visited
                ):
                    continue

                visited.add((new_row, new_col))
                new_time = max(time_so_far, grid[new_row][new_col])
                heapq.heappush(min_heap, (new_time, new_row, new_col))

        return 0