class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # dp[c] = the min path sum from the row above
        dp = [float("inf")] * COLS
        dp[0] = 0

        for r in range(ROWS):
            # for the first column, you can only arrive from directly above
            dp[0] += grid[r][0]

            for c in range(1, COLS):
                # dp[c] is from the cell above; dp[c - 1] is from the cell to the left
                dp[c] = grid[r][c] + min(dp[c], dp[c - 1])

        return dp[-1]