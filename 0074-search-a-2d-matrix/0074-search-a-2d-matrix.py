class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1
        while top <= bot:
            mid = top + (bot - top) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break

        if not (top <= bot):
            return False
        
        row = (top + bot) // 2
        target_row = matrix[row]
        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == target_row[mid]:
                return True
            elif target < target_row[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return False