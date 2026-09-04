class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda interval: interval[0])
        sorted_queries = sorted(queries)

        min_heap = [] # stores starts

        res = {}
        i = 0
        for query in sorted_queries:
            # consider all intervals with valid start time
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                heapq.heappush(min_heap, (right - left + 1, right))
                i += 1
            
            # remove all intervals which end before the query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            res[query] = min_heap[0][0] if min_heap else -1

        return [res[q] for q in queries]