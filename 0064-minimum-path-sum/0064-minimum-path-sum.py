class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dp = [float("inf")] * COLS  # dp[col] = min path sum of the col (currently)
        dp[0] = 0

        for row in range(ROWS):
            dp[0] += grid[row][0]  # only one option to get to the first column
            for col in range(1, COLS):
                # dp[col] is the cell directly above, dp[col - 1] is the cell to the left
                dp[col] = grid[row][col] + min(dp[col], dp[col - 1])

        return dp[COLS - 1]
