class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        target_start = newInterval[0]
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target_start:
                left = mid + 1
            else:
                right = mid - 1
            
        intervals.insert(left, newInterval)

        # Merge overlapping intervals
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res