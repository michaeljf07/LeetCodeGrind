class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # dp[col] = min path sum of column col
        dp = triangle[-1].copy()  # start with the last row

        # start at the second last row
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        return dp[0]
