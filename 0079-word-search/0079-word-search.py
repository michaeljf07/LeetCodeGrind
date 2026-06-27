class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def backtrack(row: int, col: int, i: int):
            if i == len(word):
                return True

            if (
                row < 0 or col < 0 or row >= ROWS or col >= COLS
                or word[i] != board[row][col] or board[row][col] == '#'
            ):
                return False

            board[row][col] = '#'
            res = any(backtrack(row + dx, col + dy, i + 1) for dx, dy in directions)

            board[row][col] = word[i]

            return res

        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0):
                    return True

        return False