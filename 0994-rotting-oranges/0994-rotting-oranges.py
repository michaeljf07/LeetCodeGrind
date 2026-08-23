from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]
        q = deque()
        fresh = 0
        time = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == FRESH:
                    fresh += 1
                elif grid[row][col] == ROTTEN:
                    q.append((row, col))

        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                row, col = q.popleft()
                for dx, dy in DIRECTIONS:
                    nr, nc = row + dx, col + dy
                    if (
                        nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        grid[nr][nc] != FRESH
                    ):
                        continue
                    
                    grid[nr][nc] = ROTTEN
                    q.append((nr, nc))
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1 