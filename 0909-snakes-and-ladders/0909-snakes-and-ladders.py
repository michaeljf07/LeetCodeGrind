class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        board.reverse()

        def squareToPosn(square: int) -> tuple[int, int]:
            row = (square - 1) // n
            col = (square - 1) % n

            # when row is odd we must "flip" the column index
            if row % 2 != 0:
                col = n - col - 1
            
            return (row, col)

        q = deque() # (square, moves)
        q.append((1, 0))
        visited = set()

        while q:
            square, moves = q.popleft()

            # roll dice
            for i in range(1, 7):
                next_square = square + i
                row, col = squareToPosn(next_square)
                if board[row][col] != -1:
                    next_square = board[row][col]

                # reached end of board
                if next_square == n * n:
                    return moves + 1
                
                if next_square not in visited:
                    visited.add(next_square)
                    q.append((next_square, moves + 1))
        
        return -1