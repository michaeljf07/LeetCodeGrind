class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        len_points = len(points)

        for i in range(len_points):
            x1, y1 = points[i]
            for j in range(len_points):
                x2, y2 = points[j]
                for k in range(len_points):
                    x3, y3 = points[k]

                    area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
                    max_area = area if area > max_area else max_area

        return max_area