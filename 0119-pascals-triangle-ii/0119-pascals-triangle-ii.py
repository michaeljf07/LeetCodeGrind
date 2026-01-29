class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows: list = [[1]]

        def genRow(n: int, prevRow: List[int]) -> List[int]:
            row: List[int] = []
            len_row: int = n + 1
            for i in range(len_row):
                if i == 0 or i == len_row - 1:
                    row.append(1)
                else:
                    row.append(prevRow[i-1] + prevRow[i])

            return row

        for i in range(1, rowIndex+1):
            rows.append(genRow(i, rows[-1]))

        return rows[-1]