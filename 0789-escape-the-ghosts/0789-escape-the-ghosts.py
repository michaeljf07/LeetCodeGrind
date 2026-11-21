class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        dist_pacman = self.calcDistance([0,0], target)
        for ghost in ghosts:
            if self.calcDistance(ghost, target) <= dist_pacman:
                return False

        return True


    def calcDistance(self, character: list[int, int], target: list[int, int]) -> int:
        """
        character: starting coordinates of pacman or the ghosts
        target: coordinates to get to

        Returns: non-diagonal distance to target
        """
        dist_rows = abs(character[0] - target[0])
        dist_cols = abs(character[1] - target[1])

        return dist_rows + dist_cols