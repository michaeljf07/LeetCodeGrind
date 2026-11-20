from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # (bottom two letters) -> options for top letter
        # e.g. "AB" -> "C"
        self.triangle_map = defaultdict(list)
        for triangle in allowed:
            self.triangle_map[triangle[:2]].append(triangle[2])

        self.failed = set()
        return self.backtrack(list(bottom), 0, [])

    # bottom: current bottom row
    # bot_idx: current index in current bottom row
    # next_row: temporary variable for the next row
    def backtrack(self, bottom: list[str], bot_idx: int, next_row: list[str]) -> bool:
        # Base Case: next row has one block means we have built the triangle
        if len(bottom) == 1:
            return True

        if bot_idx == 0:
            next_row_str = "".join(bottom)
            if next_row_str in self.failed:
                return False

        # finished building the next row
        if bot_idx == len(bottom) - 1:
            return self.backtrack(next_row, 0, [])

        key = bottom[bot_idx] + bottom[bot_idx + 1]
        for char in self.triangle_map[key]:
            next_row.append(char)  # explore
            # find valid pyramid
            if self.backtrack(bottom, bot_idx + 1, next_row):
                return True
            next_row.pop()  # backtrack

        if bot_idx == 0:
            self.failed.add("".join(bottom))

        return False
