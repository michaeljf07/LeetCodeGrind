class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # (i, j) -> min sum of the numbers along the path from top left to (i,j)
        memo = {}

        def dfs(row: int, col: int) -> int:
            # reached the bottom right corner (beginning of top down approach)
            if row == ROWS - 1 and col == COLS - 1:
                return grid[ROWS - 1][COLS - 1]
            # out of bounds check
            if row >= ROWS or col >= COLS:
                return float("inf") 

            if (row, col) in memo:
                return memo[(row, col)]

            # the next cell is either below or to the right of the current cell
            memo[(row, col)] = grid[row][col] + min(dfs(row + 1, col), dfs(row, col + 1))
            return memo[(row, col)]

        return dfs(0, 0)