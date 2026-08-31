class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
        memo = {} # (row, col) -> longest path including this cell
        longest = 0


        def dfs(row: int, col: int, prev_val: int):
            if (
                row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                prev_val >= matrix[row][col]
            ):
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            res = 1 # the current cell counts in the path
            for dx, dy in DIRECTIONS:
                res = max(res, 1 + dfs(row + dx, col + dy, matrix[row][col]))

            memo[(row, col)] = res
            return res

        
        for row in range(ROWS):
            for col in range(COLS):
                longest = max(longest, dfs(row, col, float("-inf")))
        
        return longest
