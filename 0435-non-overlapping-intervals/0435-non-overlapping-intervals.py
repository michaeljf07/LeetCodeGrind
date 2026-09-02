class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda pair: pair[0])
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            # interval does not overlap with any previous interval
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
                # since the intervals are sorted, a non-overlapping interval
                # cannot have a start before the smallest end
                prev_end = min(prev_end, end)

        return res 