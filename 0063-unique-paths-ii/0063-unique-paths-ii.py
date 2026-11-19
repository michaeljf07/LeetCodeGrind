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
                # already defined base case above
                if row == 0 and col == 0:
                    continue
                # skip squares that are obstacles
                if obstacleGrid[row][col] == OBSTACLE:
                    continue
                
                from_left = dp[row][col - 1] if col > 0 else 0
                from_top = dp[row - 1][col] if row > 0 else 0
                dp[row][col] = from_left + from_top

        return dp[ROWS - 1][COLS - 1]
