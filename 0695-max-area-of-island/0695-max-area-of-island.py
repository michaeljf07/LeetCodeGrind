class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(row: int, col: int):
            if (
                row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                grid[row][col] == 0 or
                (row, col) in visited
            ):
                return 0

            visited.add((row, col))

            traverse = sum([dfs(row + dx, col + dy) for dx, dy in DIRECTIONS])

            return 1 + traverse

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                max_area = max(max_area, dfs(row, col))

        return max_area

            