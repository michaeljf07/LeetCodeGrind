class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        LAND, WATER = 0, 1
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]

        count = 0
        
        def dfs(row: int, col: int):
            if (
                row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                grid[row][col] != LAND
            ):
                return

            grid[row][col] = 1

            for dx, dy in DIRECTIONS:
                dfs(row + dx, col + dy)
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row == 0 or col == 0 or row == ROWS - 1 or col == COLS - 1) and grid[row][col] == LAND:
                    dfs(row, col)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == LAND:
                    count += 1
                    dfs(row, col)

        return count
