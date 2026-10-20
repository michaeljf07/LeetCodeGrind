class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        We notice that rotating matrix clockwise is same as the
        flipping the matrix vertically and then transposing it
        """
        n = len(matrix)

        matrix.reverse() # flip vertically
        # by definition of transpose, matrix[i][j] = matrix[j][i]
        for row in range(n):
            for col in range(row, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]