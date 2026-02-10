class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        def getCol(matrix: List[List[int]], colNum: int) -> List[int]:
            col = []
            for row in matrix:
                col.append(row[colNum])
            return col

        for r in range(len(matrix)):
            row = matrix[r]
            min_row = min(row)
            
            for c in range(len(row)):
                num = row[c]
                
                if num == min_row:
                    column_elements = getCol(matrix, c)
                    max_col = max(column_elements)
                    
                    if num == max_col:
                        ans.append(num)

        return ans