class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda balloon: balloon[0]) # sort by starting x coord

        arrows = 1
        end = points[0][1]

        for balloon in points[1:]:
            # balloons are not overlapping -> require another arrow
            if balloon[0] > end:
                arrows += 1
                end = balloon[1]
            else:
                end = min(end, balloon[1])
        
        return arrows