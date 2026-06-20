class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0

        def dfs(row: int, col: int):
            if (
                row < 0 or col < 0 or row >= ROWS or col >= COLS or
                grid[row][col] == '0'
            ):
                return

            # convert current position to water to prevent infinite loops
            grid[row][col] = '0'
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    dfs(row, col)
                    num_islands += 1
        
        return num_islands