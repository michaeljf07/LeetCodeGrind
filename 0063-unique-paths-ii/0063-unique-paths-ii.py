class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        SPACE, OBSTACLE = 0, 1

        if obstacleGrid[0][0] == OBSTACLE:
            return 0

        dp = [[0] * COLS for _ in range(ROWS)]
        dp[0][0] = 1

        for row in range(ROWS):
            for col in range(COLS):
                if (row == 0 and col == 0) or obstacleGrid[row][col] == OBSTACLE:
                    continue
                # since we initalize all dp values to 0, we don't have to check for obstacles
                from_top = dp[row - 1][col] if row > 0 else 0
                from_left = dp[row][col - 1] if col > 0 else 0
                dp[row][col] = from_top + from_left

        return dp[ROWS - 1][COLS - 1]
