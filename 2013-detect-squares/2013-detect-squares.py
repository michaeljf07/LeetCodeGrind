class DetectSquares:

    def __init__(self):
        self.points = []
        self.points_count = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.points.append(point)
        self.points_count[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        count = 0
        px, py = point
        for x, y in self.points:
            if (abs(px - x) != abs(py - y)) or px == x or py == y:
                continue
            count += self.points_count[(x, py)] * self.points_count[(px, y)]

        return count

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)