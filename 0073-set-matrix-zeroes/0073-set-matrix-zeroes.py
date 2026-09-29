class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        first_col_has_zero = False  # needed because matrix[0][0] overlaps first row and col

        for row in range(ROWS):
            # check if first col has zero
            if matrix[row][0] == 0:
                first_col_has_zero = True

            for col in range(1, COLS):
                # flag rows and cols with zeros
                # use the first row to track cols, first col to track rows
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # edit inner matrix to avoid overwriting flags
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # edit the first row if necessary
        if matrix[0][0] == 0:
            for col in range(COLS):
                matrix[0][col] = 0

        # edit the first col if necessary
        if first_col_has_zero:
            for row in range(ROWS):
                matrix[row][0] = 0
