class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]

        def capture(row: int, col: int):
            if (
                row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                board[row][col] != 'O'
            ):
                return

            board[row][col] = 'T'
            for dx, dy in DIRECTIONS:
                capture(row + dx, col + dy)
        
        for row in range(ROWS):
            if board[row][0] == 'O':
                capture(row, 0)
            if board[row][COLS - 1] == 'O':
                capture(row, COLS - 1)

        for col in range(COLS):
            if board[0][col] == 'O':
                capture(0, col)
            if board[ROWS - 1][col] == 'O':
                capture(ROWS - 1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'