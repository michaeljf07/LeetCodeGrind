class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addCell(row: int, col: int):
            if (
                min(row, col) < 0 or row >= ROWS or col >= COLS or
                (row, col) in visited or grid[row][col] == -1
            ):
                return

            visited.add((row, col))
            q.append([row, col])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append([row, col])
                    visited.add((row, col))

        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                addCell(row + 1, col)
                addCell(row - 1, col)
                addCell(row, col + 1)
                addCell(row, col - 1)
            dist += 1
