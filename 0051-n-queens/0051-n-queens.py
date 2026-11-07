class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        cols = set()
        pos_diag = set() # determined by (row + col)
        neg_diag = set() # determined by (row - col)

        res = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(row: int):
            # we have filled the (n - 1)th row with a valid solution
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for col in range(n):
                if (col in cols) or (row + col in pos_diag) or (row - col in neg_diag):
                    continue
                
                # add queen to this spot
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = 'Q'
                backtrack(row + 1)

                # skip this spot 
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = '.'
            
        backtrack(0)
        return res