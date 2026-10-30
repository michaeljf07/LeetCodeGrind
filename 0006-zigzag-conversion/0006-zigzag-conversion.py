class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < numRows:
            return s
        
        row_idx = 0
        direction = 1 # 1 for up, -1 for down
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[row_idx].append(char)
            if row_idx == 0:
                direction = 1
            elif row_idx == numRows - 1:
                direction = -1
            row_idx += direction

        for i in range(numRows):
            rows[i] = "".join(rows[i])

        return "".join(rows)