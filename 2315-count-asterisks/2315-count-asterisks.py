class Solution:
    def countAsterisks(self, s: str) -> int:
        ignoring = False
        count = 0

        for char in s:
            if char == '|':
                ignoring = not ignoring
                
            if not ignoring and char == '*':
                count += 1

        return count
            