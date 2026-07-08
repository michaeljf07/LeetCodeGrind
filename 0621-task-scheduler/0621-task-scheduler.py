from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = 1 + count.get(task, 0)

        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        deq = deque() # pairs of [-cnt, idle_time]

        while max_heap or deq:
            time += 1
        
            if not max_heap:
                time = deq[0][1]
            else:
                count = 1 + heapq.heappop(max_heap) # decrement frequency
                if count:
                    deq.append([count, time + n])
            
            if deq and deq[0][1] == time:
                heapq.heappush(max_heap, deq.popleft()[0])

        return time